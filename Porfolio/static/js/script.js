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


    $('#search-ticket').on('keyup', function (event) {
      event.preventDefault()
      var query = $('#search-ticket').val()
      if (query != '') {
        $('#ticket-main-content').css('display', 'flex')
        $('#main-ticket-container').css('display', 'none')

        //   console.log('welcome')
        // console.log(query);
        $.ajax({
          method: 'POST',
          url: '/ticket/api/search/'+query,
          contentType: 'application/json',
          data: {},
          success: function (response) {
            // console.log(response)
            var resultsContainer = $('#ticket-main-content')
            resultsContainer.empty()
            if (response.length > 0) {
              // console.log(response);
              response.forEach(function (result) {
                // console.log(result)
                var ticketHtml =
                  '<div class="col-xs-12 col-md-6 col-sm-12 inside-allticket pt-2">' +
                  '<div class="allticket-left">' +
                  '<p>Name:' +
                  result.fields.name +
                  '</p>' +
                  '<p>Type:' +
                  result.fields.ticket_type +
                  '</p>' +
                  '<p>Price: &#x20a6;' +
                  result.fields.price +
                  '</p>' +
                  '<p>Remaining tickets:' +
                  result.fields.quantity_available +
                  '</p>'
                if (result.fields.quantity_available > 0) {
                  ticketHtml +=
                    '<a type="button" class="purchase-button" href="/payment/ticket/' +
                    result.pk +
                    '/purchase/">Purchase</a>'
                } else {
                  ticketHtml += '<p>Sold Out</p>'
                }
                ticketHtml +=
                  '</div>' +
                  '<div class="allticket-right" style="background-image:url(/media/' +
                  result.fields.img +
                  ');">' +
                  '</div>' +
                  '</div>'

                resultsContainer.append(ticketHtml)
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
      } else {
        $('#ticket-main-content').css('display', 'none')
        $('#main-ticket-container').css('display', 'flex')
      }
    })




});