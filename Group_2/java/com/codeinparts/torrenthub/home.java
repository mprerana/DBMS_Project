package com.codeinparts.torrenthub;

import android.content.Intent;
import android.support.design.widget.TabLayout;
import android.support.v4.content.ContextCompat;
import android.support.v4.view.ViewPager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.SearchView;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;

public class home extends AppCompatActivity {


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);
        Toolbar toolbar=findViewById(R.id.toolbar1);
        getActionBar();
        setSupportActionBar(toolbar);
        Window window=this.getWindow();
        window.clearFlags(WindowManager.LayoutParams.FLAG_TRANSLUCENT_STATUS);
        window.addFlags(WindowManager.LayoutParams.FLAG_DRAWS_SYSTEM_BAR_BACKGROUNDS);
        window.setStatusBarColor(ContextCompat.getColor(this,R.color.colorPrimaryDark));
        PagerAdapter pagerAdapter=new PagerAdapter(getSupportFragmentManager());
        pagerAdapter.addFragent(new movieFragment(),"Movies");
        pagerAdapter.addFragent(new gamesFragment(),"Games");
        pagerAdapter.addFragent(new seriesFragment(),"Series");
        pagerAdapter.addFragent(new bookFragment(),"Books");
        pagerAdapter.addFragent(new musicFragment(),"add");
        pagerAdapter.addFragent(new homeFragment(),"Server");
        ViewPager mviewPager=(ViewPager)findViewById(R.id.viewPager1);
        TabLayout mtabLayout=(TabLayout)findViewById(R.id.sliding_tab);
        mviewPager.setAdapter(pagerAdapter);
        mtabLayout.setupWithViewPager(mviewPager);
    }

    @Override
    public boolean onCreateOptionsMenu(final Menu menu) {
        MenuInflater menuInflater=getMenuInflater();
        menuInflater.inflate(R.menu.toolbar_menu,menu);
        final MenuItem menuItem=menu.findItem(R.id.SearchMenuItem);
        SearchView searchView= (SearchView) menuItem.getActionView();
        searchView.setOnSearchClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                setItemVisibility(menu,menuItem,false);
            }
        });
        searchView.setOnCloseListener(new SearchView.OnCloseListener() {
            @Override
            public boolean onClose() {
                setItemVisibility(menu,menuItem,true);
                return false;
            }
        });
        menuItem.setOnActionExpandListener(new MenuItem.OnActionExpandListener() {
            @Override
            public boolean onMenuItemActionExpand(MenuItem item) {
                return true;
            }

            @Override
            public boolean onMenuItemActionCollapse(MenuItem item) {
                return true;
            }
        });
        System.out.println("Menu created");
        return true;

    }

    @Override
    public  boolean onOptionsItemSelected(MenuItem item){
        int res_id=item.getItemId();
        switch (res_id){
            case R.id.downloadMenuItem:
                Intent intent=new Intent(this,Downloads.class);
                this.startActivity(intent);
                break;
            case R.id.SettingsMenuItem:
                Intent intent0=new Intent(this,Settings.class);
                this.startActivity(intent0);
                break;
            case R.id.SearchMenuItem:

                break;
        }
        return true;
    }

    private void setItemVisibility(Menu menu,MenuItem exc,boolean vis){
        for(int i =0 ;i< menu.size();++i){
            MenuItem item=menu.getItem(i);
            if(item!=exc){
                item.setVisible(vis);
            }
        }
    }

}









