describe("empty spec", () => {
  it("passes", () => {
    cy.visit("http://localhost:8501/");
    cy.get(
      ":nth-child(2) > .stNumberInput > .css-1rvyln1 > .st-bd > .st-b3 > .st-bc"
    ).type(205);
    cy.get(
      ":nth-child(3) > .stNumberInput > .css-1rvyln1 > .st-bd > .st-b3 > .st-bc"
    ).type(2);
    cy.get(
      ":nth-child(4) > .stNumberInput > .css-1rvyln1 > .st-bd > .st-b3 > .st-bc"
    ).type(0);
    cy.get("code").invoke("text").and("equal", "212533.42002884124");
  });
});
