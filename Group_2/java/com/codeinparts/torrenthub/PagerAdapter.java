package com.codeinparts.torrenthub;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentPagerAdapter;

import java.util.ArrayList;

public class PagerAdapter extends FragmentPagerAdapter {
    private ArrayList<String> tabTitles =new ArrayList<String>();
    private ArrayList<Fragment> fragments = new ArrayList<Fragment>();
    public PagerAdapter(FragmentManager fragmentManager){
        super(fragmentManager);
    }

    @Override
    public Fragment getItem(int i) {
        System.out.println(0);
        return fragments.get(i);
    }

    public  void addFragent(Fragment fragment,String title){
        this.fragments.add(fragment);
        this.tabTitles.add(title);
    }
    @Override
    public int getCount() {
        return fragments.size();
    }

    @Override
    public CharSequence getPageTitle(int position) {
        return tabTitles.get(position);
    }
}
