pub fn borrowing_sample () {
  let mut a = 10; // ref_count == 0

  let b = &a; 
  // let c = &mut a;

  // println!("{a} {b} {c}");
}