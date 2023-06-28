$(document).ready(function() {
    // var search_query = $('#search-event').val()
    
    $('#search-event').on('keyup', function (event) {
      event.preventDefault()
      var query = $('#search-event').val()
      if (query != '') {
            $('#result-main-content').removeClass('remove-content')
            $('#main-content').addClass('remove-content')

          //   console.log('welcome')
            // console.log(query);
            $.ajax({
              method: 'POST',
              url: '/api/events/search/'+query,
              contentType: 'application/json',
              data: {},
              success: function (response) {
                // console.log(response)
                var resultsContainer = $('#search-result-container')
                resultsContainer.empty()
                if (response.length > 0) {
                  // console.log(response);
                  response.forEach(function (result) {
                      console.log(result);
                    resultsContainer.append(
                      '<div class="col-xs-12 col-md-6 event-container" id="event" style="background-image:url(/media/' +
                        result.fields.img +
                        ');">\
                          <div class="start-date" style="overflow: hidden; white-space:wrap;padding:0 3px">\
                          <h2>' +
                        moment(result.fields.start)
                          .tz('GMT')
                          .format('MMM. D, YYYY, h:mm a') +
                        '</h2>\
                          </div>\
                          <div class="description">\
                          <h3><a href="get_event/' +
                        result.fields.id +
                        '">' +
                        result.fields.name +
                        '</a></h3>\
                          <p>' +
                        result.fields.location +
                        '</p>\
                          <button class="buy" >\
                              <a href="get_event/' +
                        result.fields.id +
                        '">\
                              Get Ticket\
                              </a>\
                          </button>\
                          </div>\
                      </div>'
                    )
                  })
                } else {
                  resultsContainer.append('<p>No results found.</p>')
                }
              },
              error: function () {
                $('#search-result-container').html(
                  'An error occurred while searching.'
                )
              },
            })
      }else{
        $('#main-content').removeClass('remove-content')
        $('#result-main-content').addClass('remove-content')
      }
    })
});