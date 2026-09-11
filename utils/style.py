import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        /* =========================================
           GLOBAL APP
        ========================================= */

        .stApp {
            background:
                radial-gradient(
                    circle at 5% 5%,
                    rgba(79, 70, 229, 0.20),
                    transparent 28%
                ),
                radial-gradient(
                    circle at 95% 10%,
                    rgba(14, 165, 233, 0.15),
                    transparent 28%
                ),
                linear-gradient(
                    135deg,
                    #080d1a 0%,
                    #0b1220 50%,
                    #0f172a 100%
                );

            color: #f8fafc;
        }


        /* =========================================
           MAIN CONTENT
        ========================================= */

        .block-container {
            max-width: 1250px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }


        /* =========================================
           SIDEBAR
        ========================================= */

        [data-testid="stSidebar"] {
            background:
                linear-gradient(
                    180deg,
                    #111827 0%,
                    #0b1120 100%
                );

            border-right:
                1px solid rgba(255, 255, 255, 0.08);
        }


        [data-testid="stSidebar"] * {
            color: #f8fafc;
        }


        /* =========================================
           HEADINGS
        ========================================= */

        h1,
        h2,
        h3 {
            color: #f8fafc !important;
        }


        h1 {
            font-weight: 800 !important;
            letter-spacing: -1px;
        }


        h2 {
            font-weight: 750 !important;
        }


        h3 {
            font-weight: 700 !important;
        }


        /* =========================================
           HERO CARD
        ========================================= */

        .hero {
            padding: 42px;
            margin-bottom: 30px;

            border-radius: 28px;

            background:
                linear-gradient(
                    135deg,
                    rgba(79, 70, 229, 0.96),
                    rgba(37, 99, 235, 0.90),
                    rgba(14, 165, 233, 0.82)
                );

            border:
                1px solid rgba(255, 255, 255, 0.16);

            box-shadow:
                0 25px 60px rgba(0, 0, 0, 0.35);
        }


        .hero-small {
            color: rgba(255, 255, 255, 0.78);

            font-size: 13px;

            font-weight: 700;

            letter-spacing: 1.8px;

            margin-bottom: 10px;
        }


        .hero-title {
            color: white;

            font-size: 44px;

            font-weight: 850;

            line-height: 1.1;

            margin-bottom: 16px;
        }


        .hero-text {
            color: rgba(255, 255, 255, 0.90);

            font-size: 17px;

            line-height: 1.65;

            max-width: 800px;
        }


        /* =========================================
           FEATURE CARDS
        ========================================= */

        .feature-card {
            min-height: 190px;

            padding: 25px;

            border-radius: 20px;

            background:
                linear-gradient(
                    145deg,
                    rgba(30, 41, 59, 0.96),
                    rgba(15, 23, 42, 0.96)
                );

            border:
                1px solid rgba(255, 255, 255, 0.08);

            box-shadow:
                0 12px 30px rgba(0, 0, 0, 0.24);
        }


        .feature-icon {
            font-size: 34px;

            margin-bottom: 12px;
        }


        .feature-title {
            color: white;

            font-size: 20px;

            font-weight: 750;

            margin-bottom: 9px;
        }


        .feature-text {
            color: #cbd5e1;

            font-size: 14px;

            line-height: 1.65;
        }


        /* =========================================
           STAT CARDS
        ========================================= */

        .stat-card {
            padding: 22px;

            min-height: 125px;

            text-align: center;

            border-radius: 18px;

            background:
                rgba(15, 23, 42, 0.90);

            border:
                1px solid rgba(255, 255, 255, 0.08);

            box-shadow:
                0 10px 25px rgba(0, 0, 0, 0.20);
        }


        .stat-number {
            color: white;

            font-size: 27px;

            font-weight: 800;

            margin-top: 5px;
        }


        .stat-label {
            color: #94a3b8;

            font-size: 13px;

            margin-top: 5px;
        }


        /* =========================================
           SECTION LABEL
        ========================================= */

        .section-label {
            color: #a5b4fc;

            font-size: 12px;

            font-weight: 800;

            text-transform: uppercase;

            letter-spacing: 1.7px;

            margin-bottom: 7px;
        }


        /* =========================================
           INSIGHT CARD
        ========================================= */

        .insight-card {
            padding: 25px;

            margin-top: 25px;

            border-radius: 20px;

            background:
                linear-gradient(
                    135deg,
                    rgba(30, 41, 59, 0.96),
                    rgba(49, 46, 129, 0.40)
                );

            border:
                1px solid rgba(129, 140, 248, 0.25);

            box-shadow:
                0 12px 30px rgba(0, 0, 0, 0.20);
        }


        .insight-title {
            color: white;

            font-size: 20px;

            font-weight: 750;
        }


        .insight-text {
            color: #cbd5e1;

            line-height: 1.7;

            margin-top: 10px;
        }


        /* =========================================
           BUTTONS
        ========================================= */

        .stButton > button {
            border-radius: 12px !important;

            min-height: 44px;

            font-weight: 650 !important;

            border:
                1px solid rgba(255, 255, 255, 0.12) !important;

            transition:
                transform 0.15s ease,
                box-shadow 0.15s ease;
        }


        .stButton > button:hover {
            transform: translateY(-2px);

            box-shadow:
                0 8px 22px rgba(0, 0, 0, 0.28);
        }


        /* =========================================
           INPUT BOXES
        ========================================= */

        input,
        textarea {
            border-radius: 12px !important;
        }


        /* =========================================
           DIVIDERS
        ========================================= */

        hr {
            border-color:
                rgba(255, 255, 255, 0.08) !important;
        }


        /* =========================================
           FOOTER
        ========================================= */

        .footer {
            text-align: center;

            color: #64748b;

            font-size: 13px;

            margin-top: 50px;

            padding-top: 20px;

            border-top:
                1px solid rgba(255, 255, 255, 0.06);
        }


        /* =========================================
           MOBILE
        ========================================= */

        @media (max-width: 768px) {

            .hero {
                padding: 28px;
            }

            .hero-title {
                font-size: 32px;
            }

            .hero-text {
                font-size: 15px;
            }

        }

        </style>
        """,
        unsafe_allow_html=True
    )
