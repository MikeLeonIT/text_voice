$('[data-update]').each(function() {
  var self = $(this);
  var target = self.data('update');
  var refreshId =  setInterval(function() { self.load(target); }, self.data('refresh-interval'));
});