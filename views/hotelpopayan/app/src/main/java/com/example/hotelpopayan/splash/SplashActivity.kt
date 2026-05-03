package com.example.hotelpopayan.splash

import android.content.Intent
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import androidx.appcompat.app.AppCompatActivity
import com.example.hotelpopayan.R
import com.example.hotelpopayan.login.LoginActivity

class SplashActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_splash)

        Handler(Looper.getMainLooper()).postDelayed({

            // 🔥 AQUÍ VA EL FLUJO
            startActivity(Intent(this, LoginActivity::class.java))
            finish()

        }, 2500) // 2.5 segundos
    }
}