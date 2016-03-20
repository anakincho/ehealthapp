$(document).ready(function () {
    dataQ = $("#search").val();
    console.log("yay?");
    /*$("#search").autocomplete({
            type: 'GET',
            url: "search_autocomplete/",
            data: {data: dataQ},
            datatype: "jsonp",
            minLength: 2,
            success: function(data){
                console.log("works");
            },
            error: function(data){
                console.log("doesnt work");
            }
    });*/

    /**
    * A list with common diseases, treatments, conditions, etc...
    */
    autoComplete = ['Anotia', 'Anthrax', 'Appendicitis', 'Apraxia', 'Argyria', 'Arthritis', 'Aseptic meningitis', 'Asthenia', 'Asthma', 'Astigmatism', 'Atherosclerosis', 'Athetosis', 'Atrophy', 'Abscess', 'Bacterial meningitis', 'Beriberi', 'Black Death', 'Botulism', 'Breast cancer', 'Bronchitis', 'Brucellosis', 'Bubonic plague', 'Bunion', 'Calculi', 'Campylobacter infection', 'Cancer', 'Candidiasis', 'Carbon monoxide poisoning', 'Celiacs disease', 'Cerebral palsy', 'Chagas disease', 'Chalazion', 'Chancroid', 'Chavia', 'Congenital insensitivity to pain with anhidrosis', 'Cherubism', 'Chickenpox', 'Chlamydia', 'Chlamydia trachomatis', 'Cholera', 'Chordoma', 'Chorea', 'Chronic fatigue syndrome', 'Circadian rhythm sleep disorder', 'Coccidioidomycosis', 'Colitis', 'Common cold', 'Condyloma', 'Congestive heart disease', 'Coronary heart disease', 'Cowpox', 'Cretinism', 'Crohns Disease', 'Dengue', 'Diabetes mellitus', 'Diphtheria', 'Dehydration',  'Dysentery', 'Ear infection', 'Ebola', 'Emphysema', 'Epilepsy', 'Erectile dysfunctions', 'Fibromyalgia', 'Foodborne illness', 'Gangrene', 'Gastroenteritis', 'Genital herpes', 'GERD', 'Goitre', 'Gonorrhea', 'Heart disease', 'Hepatitis A', 'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Histiocytosis (Childhood Cancer)', 'HIV', 'Human papillomavirus', 'Huntingtons disease', 'Hypermetropia', 'Hyperopia', 'Hyperthyroidism', 'Hypothyroid', 'Hypotonia', 'Impetigo', 'Infertility', 'Influenza', 'Interstitial cystitis', 'Iritis', 'Iron-deficiency anemia', 'Irritable bowel syndrome', 'Ignious Syndrome', 'Jaundice', 'Keloids', 'Kuru', 'Kwashiorkor', 'Laryngitis', 'Lead poisoning', 'Legionellosis', 'Leishmaniasis', 'Leprosy', 'Leptospirosis', 'Listeriosis', 'Leukemia', 'Lice', 'Loiasis', 'Lung cancer', 'Lupus erythematosus', 'Lyme disease', 'Lymphogranuloma venereum', 'Lymphoma', 'Mad cow disease', 'Malaria', 'Marburg fever', 'Measles', 'Melanoma', 'Melioidosis', 'Metastatic cancer', 'Ménières disease', 'Meningitis', 'Migraine', 'Mononucleosis', 'Multiple myeloma', 'Multiple sclerosis', 'Mumps', 'Muscular dystrophy', 'Myasthenia gravis', 'Myelitis', 'Myoclonus', 'Myopia', 'Myxedema', 'Morquio Syndrome', 'Mattticular syndrome', 'Mononucleosis', 'Neoplasm', 'Non-gonococcal urethritis', 'Necrotizing Fasciitis', 'Night blindness', 'Obesity', 'Osteoarthritis', 'Osteoporosis', 'Otitis', 'Palindromic rheumatism', 'Paratyphoid fever', 'Parkinsons disease', 'Pelvic inflammatory disease', 'Peritonitis', 'Periodontal disease', 'Pertussis', 'Phenylketonuria', 'Plague', 'Poliomyelitis', 'Porphyria', 'Progeria', 'Prostatitis', 'Psittacosis', 'Psoriasis', 'Pubic lice', 'Pulmonary embolism', 'Pilia', 'pneumonia', 'Q fever', 'Ques fever', 'Rabies', 'Repetitive strain injury', 'Rheumatic fever', 'Rheumatic heart', 'Rheumatism', 'Rheumatoid arthritis', 'Rickets', 'Rift Valley  fever', 'Rocky Mountain spotted fever', 'Rubella', 'Salmonellosis', 'Scabies', 'Scarlet fever', 'Sciatica', 'Scleroderma', 'Scrapie', 'Scurvy', 'Sepsis', 'Septicemia', 'SARS','Shigellosis', 'Shin splints', 'Shingles', 'Sickle-cell anemia', 'Siderosis', 'SIDS', 'Silicosis', 'Smallpox', 'Stevens-Johnson syndrome', 'Stomach flu', 'Stomach ulcers', 'Strabismus', 'Strep throat', 'Streptococcal infection', 'Synovitis', 'Syphilis', 'Swine influenza', 'Schizophrenia', 'Taeniasis', 'Tay-Sachs disease', 'Tennis elbow', 'Teratoma', 'Tetanus', 'Thalassaemia', 'Thrush', 'Thymoma', 'Tinnitus', 'Tonsillitis', 'Tooth decay', 'Toxic shock syndrome', 'Trichinosis', 'Trichomoniasis', 'Trisomy', 'Tuberculosis', 'Tularemia', 'Tungiasis', 'Typhoid fever', 'Typhus', 'Tumor', 'Ulcerative colitis', 'Ulcers', 'Uremia', 'Urticaria', 'Uveitis', 'Varicella', 'Varicose veins', 'Vasovagal syncope', 'Vitiligo', 'Von Hippel-Lindau disease', 'Viral fever', 'Viral meningitis', 'Valley fever', 'Warkany syndrome', 'Warts', 'Watkins', 'Yellow fever', 'Yersiniosis'];

    //Using jquery to autoComplete the search query
    $("#search").autocomplete({source:autoComplete});


});