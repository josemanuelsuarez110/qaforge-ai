describe("Unit Tests - Basic", () => {
  test("should return true", () => {
    expect(true).toBe(true);
  });

  test("1 + 1 should equal 2", () => {
    expect(1 + 1).toBe(2);
  });

  test("Array should contain element", () => {
    const arr = [1, 2, 3];
    expect(arr).toContain(2);
  });

  test("Object should have property", () => {
    const obj = { name: "QAForge", version: "1.0" };
    expect(obj).toHaveProperty("name");
    expect(obj.name).toBe("QAForge");
  });
});
