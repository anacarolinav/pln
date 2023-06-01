
function deleteTerm(description) {
    $.ajax("/term/" + description, {
        type: "DELETE",
        success: function(data) {
            window.location.href = "/terms";
        },
        error: function(error) {
            console.error("Error:", error);
        }
    })
    //location.reload()
}

function deleteTermo(description) {
    $.ajax("/termo/" + description, {
        type: "DELETE",
        success: function(data) {
            window.location.href = "/termos";
        },
        error: function(error) {
            console.error("Error:", error);
        }
    })
    //location.reload()
}

function deleteTermino(description) {
    $.ajax("/terminos/" + description, {
        type: "DELETE",
        success: function(data) {
            window.location.href = "/terminos";
        },
        error: function(error) {
            console.error("Error:", error);
        }
    })
    //location.reload()
}

$(document).ready(function () {
    $('#example').DataTable();
});