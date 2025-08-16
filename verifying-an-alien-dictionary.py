public boolean isAlienSorted(String[] words, String order) {
        Comparator<String> comparator = (o1, o2) -> {
            int l1 = o1.length();
            int l2 = o2.length();
            int i = 0;
            while (i < l1 && i < l2) {
                int index1 = order.indexOf(o1.charAt(i));
                int index2 = order.indexOf(o2.charAt(i));
                if (index1 < index2) {
                    return -1;
                } else if (index1 > index2) {
                    return 1;
                }
                i++;
            }
            return l1 == l2 ? 0 : (i == l1 ? -1 : 1);
        };
        for (int i = 0; i < words.length - 1; i++) {
            if (comparator.compare(words[i], words[i + 1]) > 0) {
                return false;
            }
        }
        return true;
    }