import pandas as pd
import streamlit as st


def run():
    # Function to calculate scores
    def ScorePhase0(GradedChallenge1=0, GradedChallenge2=0, GradedChallenge3=0, 
                    LiveCode1=0, LiveCode2=0, LiveCode3=0, Milestone1=0):

        # Calculate weighted scores
        CalcGC1 = GradedChallenge1 * (25 / 3 / 100)
        CalcGC2 = GradedChallenge2 * (25 / 3 / 100)
        CalcGC3 = GradedChallenge3 * (25 / 3 / 100)

        CalcLC1 = LiveCode1 * (35 / 3 / 100)
        CalcLC2 = LiveCode2 * (35 / 3 / 100)
        CalcLC3 = LiveCode3 * (35 / 3 / 100)

        CalcMl = Milestone1 * 0.4

        # Total final score
        FinalScore = CalcGC1 + CalcGC2 + CalcGC3 + CalcLC1 + CalcLC2 + CalcLC3 + CalcMl

        # Prepare data for the DataFrame
        Data = {
            'Assessment': ['Graded Challenge 1', 'Graded Challenge 2', 'Graded Challenge 3', 
                        'Live Code 1', 'Live Code 2', 'Live Code 3', 'Milestone 1'],
            'Total Score': [GradedChallenge1, GradedChallenge2, GradedChallenge3, 
                            LiveCode1, LiveCode2, LiveCode3, Milestone1],
            'Weight (%)': [25 / 3, 25 / 3, 25 / 3, 35 / 3, 35 / 3, 35 / 3, 40],
            'Score': [CalcGC1, CalcGC2, CalcGC3, CalcLC1, CalcLC2, CalcLC3, CalcMl]
        }
        
        df1 = pd.DataFrame(Data)
        
        # Round values in DataFrame
        df1['Total Score'] = df1['Total Score'].round(3)
        df1['Weight (%)'] = df1['Weight (%)'].round(3)
        df1['Score'] = df1['Score'].round(3)

        return df1, round(FinalScore, 3)

    # Streamlit UI
    st.write("## Phase 0 Calculator")
    st.image('booo.png')
    st.write("Enter your scores for each assessment:")

    # Input widgets for scores
    GradedChallenge1 = st.number_input("Graded Challenge 1", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    GradedChallenge2 = st.number_input("Graded Challenge 2", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    GradedChallenge3 = st.number_input("Graded Challenge 3", min_value=0.0, max_value=100.0, value=0.0, step=0.1)

    LiveCode1 = st.number_input("Live Code 1", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    LiveCode2 = st.number_input("Live Code 2", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    LiveCode3 = st.number_input("Live Code 3", min_value=0.0, max_value=100.0, value=0.0, step=0.1)

    Milestone1 = st.number_input("Milestone 1", min_value=0.0, max_value=100.0, value=0.0, step=0.1)

    df1, final_score = ScorePhase0(GradedChallenge1, GradedChallenge2, GradedChallenge3, LiveCode1, LiveCode2, LiveCode3, Milestone1)

    cols1, cols2 = st.columns(2)
    with cols1:
        # Display the DataFrame
        st.write("### Detailed Score Breakdown:")
        st.dataframe(df1, hide_index=True)

        calculate = st.button("Calculate")
    
    with cols2:
        if calculate:
            st.write('#### **Your Final Score Calculation is:**')
            # Display the final score
            st.markdown(
                f"""
                <div style="
                    border: 2px solid #4CAF50; 
                    border-radius: 10px; 
                    padding: 10px; 
                    background-color: #f9f9f9; 
                    text-align: center; 
                    font-size: 20px; 
                    font-weight: bold; 
                    color: #4CAF50;">
                    {final_score:.2f}%
                </div>
                """,
                unsafe_allow_html=True
            )
            st.write("*Note: This calculation is based solely on the scores provided. Other factors may influence the final outcome.*")

            if final_score < 70:
                st.write("### It's not a reason to give up")
                st.image('1.jpg')
            elif 70 <= final_score < 80:
                st.write("### Now we're talking")
                st.image('2.jpg')
            elif 80 <= final_score < 95:
                st.write("### How is it possible?")
                st.image('3.jpg')
            elif final_score >= 95: 
                st.write("### A Freakin' Genius!!!")
                st.image('4.jpg')

if __name__ == "__main__":
    run()