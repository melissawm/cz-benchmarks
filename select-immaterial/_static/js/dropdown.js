document.getElementById("benchmarks").addEventListener("change", function () {
  var selectedValue = this.value;
  if (selectedValue) {
    window.location.href = selectedValue;
  }
});

document.getElementById("cryoet").addEventListener("change", function () {
  var selectedValue = this.value;
  if (selectedValue) {
    window.location.href = selectedValue;
  }
});