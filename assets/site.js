/* Register tables: search, filter, sort, expandable detail rows, chart-driven filters.
   The page is fully readable without this script; it only adds interaction. */
(function () {
  "use strict";

  function initRegister(root) {
    var table = root.querySelector("table.reg");
    if (!table) return;
    var tbody = table.tBodies[0];
    var search = root.querySelector("[data-search]");
    var filters = Array.prototype.slice.call(root.querySelectorAll("select[data-filter]"));
    var countEl = root.querySelector("[data-count]");
    var clearBtn = root.querySelector("[data-clear]");
    var pairs = [];
    Array.prototype.forEach.call(tbody.querySelectorAll("tr.row"), function (row) {
      var detail = row.nextElementSibling && row.nextElementSibling.classList.contains("detail") ? row.nextElementSibling : null;
      pairs.push({ row: row, detail: detail, text: (row.textContent + " " + (detail ? detail.textContent : "")).toLowerCase() });
      if (detail) detail.hidden = true;
      row.setAttribute("aria-expanded", "false");
      var btn = row.querySelector(".xbtn");
      function toggle() {
        var open = row.getAttribute("aria-expanded") !== "true";
        row.setAttribute("aria-expanded", open ? "true" : "false");
        if (btn) { btn.setAttribute("aria-expanded", open ? "true" : "false"); btn.textContent = open ? "Close" : "Details"; }
        if (detail) detail.hidden = !open;
      }
      row.addEventListener("click", function (e) {
        if (e.target.closest("a")) return;
        if (window.getSelection && String(window.getSelection()).length > 0) return;
        toggle();
      });
      if (btn) btn.addEventListener("click", function (e) { e.stopPropagation(); toggle(); });
    });
    var total = pairs.length;

    function apply() {
      var q = search ? search.value.trim().toLowerCase() : "";
      var shown = 0;
      pairs.forEach(function (p) {
        var ok = !q || p.text.indexOf(q) !== -1;
        filters.forEach(function (f) {
          if (!ok || !f.value) return;
          var val = p.row.getAttribute("data-" + f.getAttribute("data-filter")) || "";
          if (val.split("|").indexOf(f.value) === -1) ok = false;
        });
        p.row.hidden = !ok;
        if (p.detail) p.detail.hidden = !ok || p.row.getAttribute("aria-expanded") !== "true";
        if (ok) shown++;
      });
      if (countEl) countEl.textContent = shown === total ? total + " records" : shown + " of " + total + " records";
      if (clearBtn) clearBtn.hidden = !(q || filters.some(function (f) { return f.value; }));
    }
    if (search) search.addEventListener("input", apply);
    filters.forEach(function (f) { f.addEventListener("change", apply); });
    if (clearBtn) clearBtn.addEventListener("click", function () {
      if (search) search.value = "";
      filters.forEach(function (f) { f.value = ""; });
      apply();
    });

    Array.prototype.forEach.call(table.querySelectorAll("thead th[data-key]"), function (th, idx) {
      var b = document.createElement("button");
      b.type = "button";
      b.textContent = th.textContent;
      th.textContent = "";
      th.appendChild(b);
      b.addEventListener("click", function () {
        var key = th.getAttribute("data-key");
        var dir = th.getAttribute("aria-sort") === "ascending" ? "descending" : "ascending";
        Array.prototype.forEach.call(table.querySelectorAll("thead th"), function (o) { o.removeAttribute("aria-sort"); });
        th.setAttribute("aria-sort", dir);
        var numeric = th.hasAttribute("data-numeric");
        pairs.sort(function (a, c) {
          var x = a.row.getAttribute("data-s-" + key) || "", y = c.row.getAttribute("data-s-" + key) || "";
          var r = numeric ? (parseFloat(x) || 0) - (parseFloat(y) || 0) : x.localeCompare(y, undefined, { numeric: true });
          return dir === "ascending" ? r : -r;
        });
        pairs.forEach(function (p) { tbody.appendChild(p.row); if (p.detail) tbody.appendChild(p.detail); });
      });
    });

    root._setFilter = function (key, value) {
      var f = root.querySelector('select[data-filter="' + key + '"]');
      if (!f) return;
      filters.forEach(function (o) { o.value = ""; });
      if (search) search.value = "";
      f.value = value;
      apply();
    };
    apply();
  }

  document.querySelectorAll("[data-register]").forEach(initRegister);

  // Chart elements that narrow the register: data-set-filter="key:value"
  document.querySelectorAll("[data-set-filter]").forEach(function (el) {
    el.addEventListener("click", function () {
      var spec = el.getAttribute("data-set-filter").split(":");
      var reg = document.querySelector("[data-register]");
      if (!reg || !reg._setFilter) return;
      reg._setFilter(spec[0], spec.slice(1).join(":"));
      reg.scrollIntoView({ behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth", block: "start" });
    });
  });

  // Headshot fallback to initials if the image cannot load
  document.querySelectorAll("img[data-fallback]").forEach(function (img) {
    function fail() { var p = img.parentNode; p.textContent = img.getAttribute("data-fallback"); }
    if (img.complete && img.naturalWidth === 0) fail(); else img.addEventListener("error", fail);
  });
})();
