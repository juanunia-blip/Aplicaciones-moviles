package com.example.hotelpopayan.home

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.hotelpopayan.R

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val destacados = findViewById<RecyclerView>(R.id.recyclerDestacados)
        val promos = findViewById<RecyclerView>(R.id.recyclerPromos)

        destacados.layoutManager =
            LinearLayoutManager(this, LinearLayoutManager.HORIZONTAL, false)

        promos.layoutManager =
            LinearLayoutManager(this)

        destacados.adapter = HotelAdapter()
        promos.adapter = PromoAdapter()
    }
}