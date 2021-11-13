function replaceNumbers(t) { let l = t; for (let t = 1; t < 20; t++) l = l.replace(" ", " "); return l }
$(document).ready(function() { const t = $(".table").attr("data-ajax-url"),
        l = $(".table").attr("product-identify-argument");
    $.ajax({ url: t, data: { "Data-Identify": l }, success: function(t) { $("#table_body").html(t); let l = "";
            t.forEach(function(t) { l += `<tr"><td style="font-family: 'roboto'; class="align-middle">${t.vehicle_type}</td><td style="font-family: 'roboto'; class="align-middle">${t.make}</td><td  style="font-family: 'roboto'; class="align-middle">${t.model}</td><td style="font-family: 'roboto'; class="align-middle">${replaceNumbers(t.year)}</td></tr>` }), console.log(l), $("#table_body").html(l) } }) });