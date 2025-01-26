document.addEventListener('DOMContentLoaded', goToHeart());

function goToHeart() {
  const heart = document.getElementById('heart');
  heart.onclick = () => {
    window.location.href = `heart`;
  };
  const diabete = document.getElementById('diabete');
  diabete.onclick = () => {
    window.location.href = `diabetes`;
  };
}
