/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package Chapter2;

/**
 *
 * @author harpss
 */
public class TestRunner {
    public static void main (String[] args){
        TestRunner tester = new TestRunner();
    }
    
    public TestRunner(){
        try{
            BookTest test = new BookTest();
            test.runTest();
            LibraryTest test2 = new LibraryTest();
            test2.runTest();
            System.out.println("SUCCESS!");
        }
        catch(Exception e){
            e.printStackTrace();
            System.out.println("FAILURE!");
        }
        System.out.println(UnitTest.getNumSuccess() + " tests completed successfully");
    }
    
}
