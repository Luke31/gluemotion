import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

class JavaSourceTest {
  @Test
  void testEmptyMethod(){
    JavaSource src = new JavaSource();
    assertEquals("someString",src.emptyMethod());
  }
}