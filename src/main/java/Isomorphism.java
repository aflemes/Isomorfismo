/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author allan.lemes
 */
import io.github.innofang.graph.datasets.GraphDBDataSet;
import io.github.innofang.lib.UllmannState;
import io.github.innofang.util.MatchHelper;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;

public class Isomorphism {
    public static void main(String[] args) throws IOException, NoSuchMethodException, IllegalAccessException, InvocationTargetException, InstantiationException{
        String sourceGraphPath = "datasets/test/isomorphism/source_graph.txt";
        String targetGraphPath = "datasets/test/isomorphism/target_graph.txt";
        
        MatchHelper.testIsomorphismAlgorithm(
                targetGraphPath,
                sourceGraphPath,
                UllmannState.class,
                new GraphDBDataSet(),
                mapping -> {
                    System.out.println(mapping.toString());
                    return false;
                }
        );
    }
    
}
