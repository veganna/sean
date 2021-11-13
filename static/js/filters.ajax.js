$(document).ready(function() {
    const a = $("#Vtype").attr("data-vehicle_type-url"),
        t = $(this).val();
    $.ajax({
        url: a,
        data: {
            "data-Vtype": t
        },
        success: function(a) {
            $("#Vtype").html(a);
            let t = '<option value="">---------</option>';
            a.forEach(function(a) {
                t += `<option value="${a.vehicle_type}">${a.vehicle_type}</option>`
            }), console.log(t), $("#Vtype").html(t)
        }
    })
});

$("#Vtype").change(function() {
    const a = $("#Make").attr("data-make-url"),
        t = $(this).val();
    $.ajax({
        url: a,
        data: {
            "Data-Vtype": t
        },
        success: function(a) {
            $("#Make").html(a);
            let t = '<option value="">---------</option>';
            a.forEach(function(a) {
                t += `<option value="${a.make}">${a.make}</option>`
            }), console.log(t), $("#Make").html(t)
        }
    })
});

$("#Make").change(function() {
    const a = $("#Model").attr("data-model-url"),
        t = $("#Vtype").val(),
        o = $(this).val();
    $.ajax({
        url: a,
        data: {
            "Data-Vtype": t,
            "Data-Make": o
        },
        success: function(a) {
            $("#Model").html(a);
            let t = '<option value="">---------</option>';
            a.forEach(function(a) {
                t += `<option value="${a.model}">${a.model}</option>`
            }), $("#Model").html(t)
        }
    })
});

$("#Model").change(function() {
    const a = $("#Year").attr("data-year-url"),
        t = $("#Vtype").val(),
        o = $("#Make").val(),
        e = $(this).val();
    $.ajax({
        url: a,
        data: {
            "Data-Vtype": t,
            "Data-Make": o,
            "Data-Model": e
        },
        success: function(a) {
            $("#Year").html(a);
            let t = '<option value="">---------</option>';
            a.forEach(function(a) {
                t += `<option value="${a.year}">${a.year}</option>`
            }), $("#Year").html(t)
        }
    })
});

$("#Year").change(function() {
    const a = $("#category").attr("data-category-url"),
        t = $("#Vtype").val(),
        o = $("#Make").val(),
        e = $("#Model").val(),
        n = $(this).val();
    $.ajax({
        url: a,
        data: {
            "Data-Vtype": t,
            "Data-Make": o,
            "Data-Model": e,
            "Data-Year": n
        },
        success: function(a) {
            $("#category").html(a);
            let t = '<option value="">---------</option>';
            a.forEach(function(a) {
                t += `<option value="${a.category}">${a.category}</option>`
            }), $("#category").html(t)
        }
    })
});

$("#category").change(function() {
    const a = $("#subcategory").attr("data-subcategory-url"),
        t = $("#Vtype").val(),
        o = $("#Make").val(),
        e = $("#Model").val(),
        n = $("#Year").val(),
        l = $(this).val();
    $.ajax({
        url: a,
        data: {
            "Data-Vtype": t,
            "Data-Make": o,
            "Data-Model": e,
            "Data-Year": n,
            "Data-Category": l
        },
        success: function(a) {
            $("#subcategory").html(a);
            let t = '<option value="">---------</option>';
            a.forEach(function(a) {
                t += `<option value="${a.sub_category}">${a.sub_category}</option>`
            }), $("#subcategory").html(t)
        }
    })
});

$("#subcategory").change(function() {
    const a = $("#brand").attr("data-brand-url"),
        t = $("#Vtype").val(),
        o = $("#Make").val(),
        e = $("#Model").val(),
        n = $("#Year").val(),
        l = $("#category").val(),
        y = $(this).val();
    $.ajax({
        url: a,
        data: {
            "Data-Vtype": t,
            "Data-Make": o,
            "Data-Model": e,
            "Data-Year": n,
            "Data-Category": l,
            "Data-Subcategory": y
        },
        success: function(a) {
            $("#brand").html(a);
            let t = '<option value="">---------</option>';
            a.forEach(function(a) {
                t += `<option value="${a.brand}">${a.brand}</option>`
            }), $("#brand").html(t)
        }
    })
});