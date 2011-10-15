/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package Chapter2;

/**
 *
 * @author harpss
 */
public class LibraryTest extends UnitTest{
    
    public void runTest() throws Exception{
        Library library = new Library();
        Book expectedBook1 = new Book("Dune");
        Book expectedBook2 = new Book("Doctor Who");
        library.addBook(expectedBook1);
        library.addBook(expectedBook2);
        Book actualBook1 = library.getBook("Dune");
        Book actualBook2 = library.getBook("Doctor Who");
        assertTrue(actualBook1.title.equals("Dune"), "got book");                
        assertTrue(actualBook2.title.equals("Doctor Who"), "got book");                
    }
}
