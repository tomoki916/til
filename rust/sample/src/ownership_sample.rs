struct H2O {}
struct O2{}
struct H2{}

fn burn(_h2_1: H2, _h2_2: H2, _o2: O2) -> (H2O, H2O) {
  (H2O {}, H2O {})
}

pub fn generate_h2o () {
  let h2_1  = H2 {};
  let h2_2  = H2 {};
  let o2 = O2 {};

  let (h2o_1, h2o_2) = burn(h2_1, h2_2, o2);
}