const num = prompt('성적을 입력하세요.');
if (num >= 90) {
  if (num >= 97) {
    document.write('A+');
  } else if (94 <= num <= 96) {
    document.write('A0');
  } else {
    document.write('A-');
  }
} else if (num >= 80) {
  if (num >= 87) {
    document.write('B+');
  } else if (84 <= num <= 86) {
    document.write('B0');
  } else {
    document.write('B-');
  }
} else if (num >= 70) {
  if (num >= 77) {
    document.write('C+');
  } else if (74 <= num <= 76) {
    document.write('C0');
  } else {
    document.write('C-');
  }
} else if (num >= 60) {
  if (num >= 67) {
    document.write('D+');
  } else if (64 <= num <= 66) {
    document.write('D0');
  } else {
    document.write('D-');
  }
} else {
  document.write('F');
}
