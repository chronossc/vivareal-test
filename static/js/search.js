$( document ).ready(function() {
    var timer,
        typingInterval = 800;  //time in ms (5 seconds)

    var vehicle_query_url = "/api/vehicle/";

    var getQueryVariable = function(variable){
        var query = window.location.search.substring(1);
        var vars = query.split("&");
        for (var i=0;i<vars.length;i++) {
            var pair = vars[i].split("=");
            if(pair[0] == variable){return pair[1];}
        }
        return(false);
    };

    var editButton = function(id) {
        return `<button data-id="${id}" class="btn btn-default btn-xs"><i class="glyphicon glyphicon-edit"></i></button>`
    };

    var doSearch = function (target) {

        var value = $("#search").val(),
            table = $("#results"),
            results = $("#results").find("> tbody"),
            noResult = $("#no-results"),
            pagination = $("#pagination"),
            goNext = $("#goNext"),
            goPrevious = $("#goPrevious");

        if (!target) {
            target = vehicle_query_url;
        }
        $.get(target, {search: value})
            .done(function (data) {
                if (data.count == 0) {
                    if (!$("#results:hidden").length) {
                        table.fadeOut();
                    }
                    if (!$("#no-results:hidden").length) {
                        noResult.fadeIn();
                    }
                    if (!$("#pagination:hidden").length) {
                        pagination.fadeOut();
                    }
                } else {
                    if (!$("#results:hidden").length) {
                        table.fadeOut();
                    }
                    if (!$("#pagination:hidden").length) {
                        pagination.fadeOut();
                    }
                    results.find("tr").remove();
                    data.results.forEach(function(entry, index, array) {
                        results.append(
                            `<tr>` +
                            `  <td>${entry.type}</td>` +
                            `  <td>${entry.automaker}</td>` +
                            `  <td>${entry.model}</td>` +
                            `  <td>${entry.color}</td>` +
                            `  <td>${entry.mileage}</td>` +
                            `  <td>${entry.motor_potency}</td>` +
                            `  <td>${editButton(entry.id)}</td>` +
                            `</tr>`
                        )
                    });

                    if (data.next) {
                        goNext.data('link', data.next);
                        goNext.parent().removeClass('disabled');
                    } else {
                        goNext.parent().addClass('disabled');
                    }

                    if (data.previous) {
                        goPrevious.data('link', data.previous);
                        goPrevious.parent().removeClass('disabled');
                    } else {
                        goPrevious.parent().addClass('disabled');
                    }

                    table.fadeIn();
                    pagination.fadeIn();
                }
            })
            .fail(function () {
                console.debug("Uh ohhh! Gona fishing...");
            })
    };

    $("form").on("submit", function (e) {
        e.preventDefault();
        e.stopImmediatePropagation();
        return false;
    });

    $("#search").val(getQueryVariable("search") || '')
                .keyup(function () {
        clearTimeout(timer);
        timer = setTimeout(doSearch, typingInterval);
    });

    $("#goNext").on("click", function() {
        if (!$(this).parent().hasClass("disabled")) {
            doSearch($(this).data("link"));
        }
    });

    $("#goPrevious").on("click", function() {
        if (!$(this).parent().hasClass("disabled")) {
            doSearch($(this).data("link"));
        }
    });



    doSearch();
});
