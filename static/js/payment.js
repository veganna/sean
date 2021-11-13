let m = $("#script_data").attr("data-paypal-email");
$("#script_data").removeAttr("data-paypal-email");
let n = $("#script_data").attr("data-paypal-secret");
$("#script_data").removeAttr("data-paypal-secret");
let o = $("#script_data").attr("data-paypal-client");
$("#script_data").removeAttr("data-paypal-client");
var p = $("#script_data").attr("data-order-id");
$("#script_data").removeAttr("data-order-id");
var url = $("#script_data").attr("data-url");
$("#script_data").removeAttr("data-url");
var value_amount = $("#script_data").attr("total-price");
$("#script_data").removeAttr("total-price"), $("#script_data").removeAttr("id");
var PAYPAL_CLIENT = o,
    PAYPAL_SECRET = n,
    PAYPAL_EMAIL = m;

function getCookie(t) {
    let a = null;
    if (document.cookie && "" !== document.cookie) {
        const e = document.cookie.split(";");
        for (let r = 0; r < e.length; r++) {
            const o = e[r].trim();
            if (o.substring(0, t.length + 1) === t + "=") {
                a = decodeURIComponent(o.substring(t.length + 1));
                break
            }
        }
    }
    return a
}
const csrftoken = getCookie("csrftoken");

function completedorder() {
    fetch(url, {
        method: "POST",
        hearders: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken
        },
        body: JSON.stringify({
            order_id: p
        })
    })
}
paypal.Buttons({
    createOrder: function(t, a) {
        return a.order.create({
            purchase_units: [{
                amount: {
                    value: value_amount
                }
            }]
        })
    },
    onApprove: function(t, a) {
        return a.order.capture().then(function(t) {
            completedorder();
            window.location.href = "/payment/success";
        })
    }
}).render("#paypal-button-container");