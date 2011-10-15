/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package Chapter2;

/**
 *
 * @author harpss
 */
public class BookTest extends UnitTest{

    public void runTest()throws Exception{
        Book book = new Book("Dune");
        
        assertTrue(book.title.equals("Dune"), "checking title");
    }
    
}
