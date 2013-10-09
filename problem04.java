/*
 * problem04.java
 * 
 * Copyright 2013 Alex <alex@kludge>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


public class problem04 {

    public static boolean isPalindrome(Integer num) {

        String str = new Integer(num).toString();
        String rev = new StringBuilder(str).reverse().toString();

        if (str.compareTo(rev) == 0) {
            System.out.println(num + " is a palindrome!");
            return true;
        }

//        System.out.println(num + " is not a palindrome!");
        return false;
    }

    public static void main (String args[]) {

        Integer product = 1, max = 0;

        for (int i = 100; i < 1000; i++) {
            for (int j = 100; j < 1000; j++) {
                product = i * j;
                if (isPalindrome(product)) {
                    if (max < product) {
                        max = product;
                    }
                }
            }
        }

        System.out.println("Max: " + max);
    }
}

