package com.example.hotelpopayan.login

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.example.hotelpopayan.R
import com.example.hotelpopayan.home.MainActivity

class LoginActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContentView(R.layout.activity_login)

        title = "ESTOY EN LOGIN"

        val tvRegister = findViewById<TextView>(R.id.tvRegister)
        val btnLogin = findViewById<Button>(R.id.btnLogin)

        // 👉 Ir a registro
        tvRegister.setOnClickListener {
            startActivity(Intent(this, RegisterActivity::class.java))
        }

        // 👉 Ir al HOME (MainActivity)
        btnLogin.setOnClickListener {
            startActivity(Intent(this, MainActivity::class.java))
            finish() // opcional: evita volver al login con el botón atrás
        }
    }
}