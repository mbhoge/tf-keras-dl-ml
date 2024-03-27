# Databricks notebook source
remote_files = ["/california-housing/", "/california-housing/README.md", "/california-housing/test/", "/california-housing/test/_delta_log/", "/california-housing/test/_delta_log/.s3-optimization-0", "/california-housing/test/_delta_log/.s3-optimization-1", "/california-housing/test/_delta_log/.s3-optimization-2", "/california-housing/test/_delta_log/00000000000000000000.crc", "/california-housing/test/_delta_log/00000000000000000000.json", "/california-housing/test/_delta_log/00000000000000000001.crc", "/california-housing/test/_delta_log/00000000000000000001.json", "/california-housing/test/_delta_log/00000000000000000002.crc", "/california-housing/test/_delta_log/00000000000000000002.json", "/california-housing/test/part-00000-1f84fba0-c77d-457d-9925-b4395d56f98c-c000.snappy.parquet", "/california-housing/test/part-00000-50cb9f15-f334-4db5-af8a-dffad3a34d79-c000.snappy.parquet", "/california-housing/test/part-00000-a7be5518-4fd9-4fd0-a736-7995cce89403-c000.snappy.parquet", "/california-housing/test/part-00001-341a2c00-ef3d-4155-8850-33da19c9230e-c000.snappy.parquet", "/california-housing/test/part-00001-3fbfaa13-eedf-4878-ac88-b89a40e92f15-c000.snappy.parquet", "/california-housing/test/part-00001-abc91bd0-cece-4792-b2d6-078195b186e5-c000.snappy.parquet", "/california-housing/test/part-00002-1e733f02-c1fe-47f7-bc39-0321645d3640-c000.snappy.parquet", "/california-housing/test/part-00002-7c0fa3a6-7401-419d-ab5e-fa25e009255f-c000.snappy.parquet", "/california-housing/test/part-00002-8584a178-9b74-4bc9-95dc-6cdfe039ecae-c000.snappy.parquet", "/california-housing/test/part-00003-b63d17e3-aa03-49ca-98a5-9d662d951f83-c000.snappy.parquet", "/california-housing/test/part-00003-eae20902-424b-494a-b5a1-ab742c50533e-c000.snappy.parquet", "/california-housing/test/part-00003-eb5a09bd-21c3-4f60-905c-df3e4a84fcfe-c000.snappy.parquet", "/california-housing/train/", "/california-housing/train/_delta_log/", "/california-housing/train/_delta_log/.s3-optimization-0", "/california-housing/train/_delta_log/.s3-optimization-1", "/california-housing/train/_delta_log/.s3-optimization-2", "/california-housing/train/_delta_log/00000000000000000000.crc", "/california-housing/train/_delta_log/00000000000000000000.json", "/california-housing/train/_delta_log/00000000000000000001.crc", "/california-housing/train/_delta_log/00000000000000000001.json", "/california-housing/train/_delta_log/00000000000000000002.crc", "/california-housing/train/_delta_log/00000000000000000002.json", "/california-housing/train/part-00000-11c876ce-c6bf-43b5-8c25-4faa9681bb35-c000.snappy.parquet", "/california-housing/train/part-00000-685727d6-6cc4-4491-a0f1-021cd4341737-c000.snappy.parquet", "/california-housing/train/part-00000-d3d79ea2-9c9d-437f-9ba6-a62d548ecce7-c000.snappy.parquet", "/california-housing/train/part-00001-6e896e0f-b200-45eb-9004-207d204cd19e-c000.snappy.parquet", "/california-housing/train/part-00001-8cf0efcb-9e8f-4cf4-96a8-dda315cb338c-c000.snappy.parquet", "/california-housing/train/part-00001-c2eb54ab-82be-4c70-89f3-38a462ef36eb-c000.snappy.parquet", "/california-housing/train/part-00002-0b716e3b-0959-4f8d-b128-d4d4e73fdba1-c000.snappy.parquet", "/california-housing/train/part-00002-4081f2a8-8ca8-4ca0-9802-d83832c41b3c-c000.snappy.parquet", "/california-housing/train/part-00002-baec0479-c67a-4ca9-b5a5-161ea0ff6144-c000.snappy.parquet", "/california-housing/train/part-00003-730a5d01-189b-4502-a7e5-a46b95814503-c000.snappy.parquet", "/california-housing/train/part-00003-9d24ab5b-3846-415e-969c-7a6669638264-c000.snappy.parquet", "/california-housing/train/part-00003-d0e7772c-52f0-40da-b12c-0a64efa4355f-c000.snappy.parquet", "/california-housing/val/", "/california-housing/val/_delta_log/", "/california-housing/val/_delta_log/.s3-optimization-0", "/california-housing/val/_delta_log/.s3-optimization-1", "/california-housing/val/_delta_log/.s3-optimization-2", "/california-housing/val/_delta_log/00000000000000000000.crc", "/california-housing/val/_delta_log/00000000000000000000.json", "/california-housing/val/_delta_log/00000000000000000001.crc", "/california-housing/val/_delta_log/00000000000000000001.json", "/california-housing/val/_delta_log/00000000000000000002.crc", "/california-housing/val/_delta_log/00000000000000000002.json", "/california-housing/val/part-00000-17dffde6-147a-4815-bef3-5f9922c8ae03-c000.snappy.parquet", "/california-housing/val/part-00000-29c8d12e-c28a-4af5-a809-466455fc96ce-c000.snappy.parquet", "/california-housing/val/part-00000-f7bc9056-da95-48e6-a9eb-2ef835dcfa32-c000.snappy.parquet", "/california-housing/val/part-00001-2affb8b2-29c7-4ddd-b754-04e010fc0cf9-c000.snappy.parquet", "/california-housing/val/part-00001-3925a6a2-4a59-4167-ad50-eb26840eb186-c000.snappy.parquet", "/california-housing/val/part-00001-f7c92747-b8de-4c91-ae89-83cc99b02901-c000.snappy.parquet", "/california-housing/val/part-00002-35128221-01ea-4a72-b8d2-545b8dbf19a0-c000.snappy.parquet", "/california-housing/val/part-00002-35ca7c3a-1ffe-4aff-8453-beadb73e5611-c000.snappy.parquet", "/california-housing/val/part-00002-40e58bd7-f7a2-4e81-a2dc-b22c9f356af9-c000.snappy.parquet", "/california-housing/val/part-00003-74433790-bd6f-4c07-85af-9e95bb77741c-c000.snappy.parquet", "/california-housing/val/part-00003-eb7a956c-65a8-4840-a034-d44ec01b8004-c000.snappy.parquet", "/california-housing/val/part-00003-f5803e06-aca9-4cc5-9407-391fdd981832-c000.snappy.parquet", "/chest-xray/", "/chest-xray/README.md", "/chest-xray/test/", "/chest-xray/test/normal/", "/chest-xray/test/normal/IM-0001-0001.jpeg", "/chest-xray/test/normal/IM-0003-0001.jpeg", "/chest-xray/test/normal/IM-0005-0001.jpeg", "/chest-xray/test/normal/IM-0006-0001.jpeg", "/chest-xray/test/normal/IM-0007-0001.jpeg", "/chest-xray/test/normal/IM-0009-0001.jpeg", "/chest-xray/test/normal/IM-0010-0001.jpeg", "/chest-xray/test/normal/IM-0011-0001-0001.jpeg", "/chest-xray/test/normal/IM-0011-0001-0002.jpeg", "/chest-xray/test/normal/IM-0011-0001.jpeg", "/chest-xray/test/normal/IM-0013-0001.jpeg", "/chest-xray/test/normal/IM-0015-0001.jpeg", "/chest-xray/test/normal/IM-0016-0001.jpeg", "/chest-xray/test/normal/IM-0017-0001.jpeg", "/chest-xray/test/normal/IM-0019-0001.jpeg", "/chest-xray/test/normal/IM-0021-0001.jpeg", "/chest-xray/test/normal/IM-0022-0001.jpeg", "/chest-xray/test/normal/IM-0023-0001.jpeg", "/chest-xray/test/normal/IM-0025-0001.jpeg", "/chest-xray/test/normal/IM-0027-0001.jpeg", "/chest-xray/test/normal/IM-0028-0001.jpeg", "/chest-xray/test/normal/IM-0029-0001.jpeg", "/chest-xray/test/normal/IM-0030-0001.jpeg", "/chest-xray/test/normal/IM-0031-0001.jpeg", "/chest-xray/test/normal/IM-0033-0001-0001.jpeg", "/chest-xray/test/normal/IM-0033-0001-0002.jpeg", "/chest-xray/test/normal/IM-0033-0001.jpeg", "/chest-xray/test/normal/IM-0035-0001.jpeg", "/chest-xray/test/normal/IM-0036-0001.jpeg", "/chest-xray/test/normal/IM-0037-0001.jpeg", "/chest-xray/test/normal/IM-0039-0001.jpeg", "/chest-xray/test/normal/IM-0041-0001.jpeg", "/chest-xray/test/normal/IM-0043-0001.jpeg", "/chest-xray/test/normal/IM-0045-0001.jpeg", "/chest-xray/test/normal/IM-0046-0001.jpeg", "/chest-xray/test/normal/IM-0049-0001.jpeg", "/chest-xray/test/normal/IM-0050-0001.jpeg", "/chest-xray/test/normal/IM-0059-0001.jpeg", "/chest-xray/test/normal/IM-0061-0001.jpeg", "/chest-xray/test/normal/IM-0063-0001.jpeg", "/chest-xray/test/normal/IM-0065-0001.jpeg", "/chest-xray/test/normal/IM-0067-0001.jpeg", "/chest-xray/test/normal/IM-0069-0001.jpeg", "/chest-xray/test/normal/IM-0070-0001.jpeg", "/chest-xray/test/normal/IM-0071-0001.jpeg", "/chest-xray/test/normal/IM-0073-0001.jpeg", "/chest-xray/test/normal/IM-0075-0001.jpeg", "/chest-xray/test/normal/IM-0077-0001.jpeg", "/chest-xray/test/normal/IM-0079-0001.jpeg", "/chest-xray/test/normal/IM-0081-0001.jpeg", "/chest-xray/test/pneumonia/", "/chest-xray/test/pneumonia/person100_bacteria_475.jpeg", "/chest-xray/test/pneumonia/person100_bacteria_477.jpeg", "/chest-xray/test/pneumonia/person100_bacteria_478.jpeg", "/chest-xray/test/pneumonia/person100_bacteria_479.jpeg", "/chest-xray/test/pneumonia/person100_bacteria_480.jpeg", "/chest-xray/test/pneumonia/person100_bacteria_481.jpeg", "/chest-xray/test/pneumonia/person100_bacteria_482.jpeg", "/chest-xray/test/pneumonia/person101_bacteria_483.jpeg", "/chest-xray/test/pneumonia/person101_bacteria_484.jpeg", "/chest-xray/test/pneumonia/person101_bacteria_485.jpeg", "/chest-xray/test/pneumonia/person101_bacteria_486.jpeg", "/chest-xray/test/pneumonia/person102_bacteria_487.jpeg", "/chest-xray/test/pneumonia/person103_bacteria_488.jpeg", "/chest-xray/test/pneumonia/person103_bacteria_489.jpeg", "/chest-xray/test/pneumonia/person103_bacteria_490.jpeg", "/chest-xray/test/pneumonia/person104_bacteria_491.jpeg", "/chest-xray/test/pneumonia/person104_bacteria_492.jpeg", "/chest-xray/test/pneumonia/person108_bacteria_504.jpeg", "/chest-xray/test/pneumonia/person108_bacteria_506.jpeg", "/chest-xray/test/pneumonia/person108_bacteria_507.jpeg", "/chest-xray/test/pneumonia/person108_bacteria_511.jpeg", "/chest-xray/test/pneumonia/person109_bacteria_512.jpeg", "/chest-xray/test/pneumonia/person109_bacteria_513.jpeg", "/chest-xray/test/pneumonia/person109_bacteria_517.jpeg", "/chest-xray/test/pneumonia/person109_bacteria_519.jpeg", "/chest-xray/test/pneumonia/person109_bacteria_522.jpeg", "/chest-xray/test/pneumonia/person109_bacteria_523.jpeg", "/chest-xray/test/pneumonia/person109_bacteria_526.jpeg", "/chest-xray/test/pneumonia/person109_bacteria_527.jpeg", "/chest-xray/test/pneumonia/person109_bacteria_528.jpeg", "/chest-xray/test/pneumonia/person10_virus_35.jpeg", "/chest-xray/test/pneumonia/person110_bacteria_531.jpeg", "/chest-xray/test/pneumonia/person111_bacteria_533.jpeg", "/chest-xray/test/pneumonia/person111_bacteria_534.jpeg", "/chest-xray/test/pneumonia/person111_bacteria_535.jpeg", "/chest-xray/test/pneumonia/person111_bacteria_536.jpeg", "/chest-xray/test/pneumonia/person111_bacteria_537.jpeg", "/chest-xray/test/pneumonia/person112_bacteria_538.jpeg", "/chest-xray/test/pneumonia/person112_bacteria_539.jpeg", "/chest-xray/test/pneumonia/person113_bacteria_540.jpeg", "/chest-xray/test/pneumonia/person113_bacteria_541.jpeg", "/chest-xray/test/pneumonia/person113_bacteria_542.jpeg", "/chest-xray/test/pneumonia/person113_bacteria_543.jpeg", "/chest-xray/test/pneumonia/person114_bacteria_544.jpeg", "/chest-xray/test/pneumonia/person114_bacteria_545.jpeg", "/chest-xray/test/pneumonia/person114_bacteria_546.jpeg", "/chest-xray/test/pneumonia/person117_bacteria_553.jpeg", "/chest-xray/test/pneumonia/person117_bacteria_556.jpeg", "/chest-xray/test/pneumonia/person117_bacteria_557.jpeg", "/chest-xray/train/", "/chest-xray/train/normal/", "/chest-xray/train/normal/IM-0115-0001.jpeg", "/chest-xray/train/normal/IM-0117-0001.jpeg", "/chest-xray/train/normal/IM-0119-0001.jpeg", "/chest-xray/train/normal/IM-0122-0001.jpeg", "/chest-xray/train/normal/IM-0125-0001.jpeg", "/chest-xray/train/normal/IM-0127-0001.jpeg", "/chest-xray/train/normal/IM-0128-0001.jpeg", "/chest-xray/train/normal/IM-0129-0001.jpeg", "/chest-xray/train/normal/IM-0131-0001.jpeg", "/chest-xray/train/normal/IM-0133-0001.jpeg", "/chest-xray/train/normal/IM-0135-0001.jpeg", "/chest-xray/train/normal/IM-0137-0001.jpeg", "/chest-xray/train/normal/IM-0140-0001.jpeg", "/chest-xray/train/normal/IM-0141-0001.jpeg", "/chest-xray/train/normal/IM-0143-0001.jpeg", "/chest-xray/train/normal/IM-0145-0001.jpeg", "/chest-xray/train/normal/IM-0147-0001.jpeg", "/chest-xray/train/normal/IM-0149-0001.jpeg", "/chest-xray/train/normal/IM-0151-0001.jpeg", "/chest-xray/train/normal/IM-0152-0001.jpeg", "/chest-xray/train/normal/IM-0154-0001.jpeg", "/chest-xray/train/normal/IM-0156-0001.jpeg", "/chest-xray/train/normal/IM-0158-0001.jpeg", "/chest-xray/train/normal/IM-0160-0001.jpeg", "/chest-xray/train/normal/IM-0162-0001.jpeg", "/chest-xray/train/normal/IM-0164-0001.jpeg", "/chest-xray/train/normal/IM-0166-0001.jpeg", "/chest-xray/train/normal/IM-0168-0001.jpeg", "/chest-xray/train/normal/IM-0170-0001.jpeg", "/chest-xray/train/normal/IM-0172-0001.jpeg", "/chest-xray/train/normal/IM-0176-0001.jpeg", "/chest-xray/train/normal/IM-0177-0001.jpeg", "/chest-xray/train/normal/IM-0178-0001.jpeg", "/chest-xray/train/normal/IM-0180-0001.jpeg", "/chest-xray/train/normal/IM-0182-0001.jpeg", "/chest-xray/train/normal/IM-0183-0001.jpeg", "/chest-xray/train/normal/IM-0185-0001.jpeg", "/chest-xray/train/normal/IM-0187-0001.jpeg", "/chest-xray/train/normal/IM-0189-0001.jpeg", "/chest-xray/train/normal/IM-0191-0001.jpeg", "/chest-xray/train/normal/IM-0193-0001.jpeg", "/chest-xray/train/normal/IM-0195-0001.jpeg", "/chest-xray/train/normal/IM-0199-0001.jpeg", "/chest-xray/train/normal/IM-0201-0001.jpeg", "/chest-xray/train/normal/IM-0203-0001.jpeg", "/chest-xray/train/normal/IM-0205-0001.jpeg", "/chest-xray/train/normal/IM-0206-0001.jpeg", "/chest-xray/train/normal/IM-0207-0001.jpeg", "/chest-xray/train/normal/IM-0209-0001.jpeg", "/chest-xray/train/normal/IM-0210-0001.jpeg", "/chest-xray/train/normal/IM-0211-0001.jpeg", "/chest-xray/train/normal/IM-0213-0001.jpeg", "/chest-xray/train/normal/IM-0214-0001.jpeg", "/chest-xray/train/normal/IM-0215-0001.jpeg", "/chest-xray/train/normal/IM-0216-0001.jpeg", "/chest-xray/train/normal/IM-0217-0001.jpeg", "/chest-xray/train/normal/IM-0218-0001.jpeg", "/chest-xray/train/normal/IM-0219-0001.jpeg", "/chest-xray/train/normal/IM-0220-0001.jpeg", "/chest-xray/train/normal/IM-0221-0001.jpeg", "/chest-xray/train/normal/IM-0222-0001.jpeg", "/chest-xray/train/normal/IM-0223-0001.jpeg", "/chest-xray/train/normal/IM-0224-0001.jpeg", "/chest-xray/train/normal/IM-0225-0001.jpeg", "/chest-xray/train/normal/IM-0226-0001.jpeg", "/chest-xray/train/normal/IM-0227-0001.jpeg", "/chest-xray/train/normal/IM-0228-0001.jpeg", "/chest-xray/train/normal/IM-0229-0001.jpeg", "/chest-xray/train/normal/IM-0230-0001.jpeg", "/chest-xray/train/normal/IM-0231-0001.jpeg", "/chest-xray/train/normal/IM-0234-0001.jpeg", "/chest-xray/train/normal/IM-0235-0001.jpeg", "/chest-xray/train/normal/IM-0236-0001.jpeg", "/chest-xray/train/normal/IM-0237-0001.jpeg", "/chest-xray/train/normal/IM-0238-0001.jpeg", "/chest-xray/train/normal/IM-0239-0001.jpeg", "/chest-xray/train/normal/IM-0240-0001.jpeg", "/chest-xray/train/normal/IM-0241-0001.jpeg", "/chest-xray/train/normal/IM-0242-0001.jpeg", "/chest-xray/train/normal/IM-0243-0001.jpeg", "/chest-xray/train/normal/IM-0244-0001.jpeg", "/chest-xray/train/normal/IM-0245-0001.jpeg", "/chest-xray/train/normal/IM-0248-0001.jpeg", "/chest-xray/train/normal/IM-0249-0001.jpeg", "/chest-xray/train/normal/IM-0250-0001.jpeg", "/chest-xray/train/normal/IM-0251-0001.jpeg", "/chest-xray/train/normal/IM-0253-0001.jpeg", "/chest-xray/train/normal/IM-0255-0001.jpeg", "/chest-xray/train/normal/IM-0256-0001.jpeg", "/chest-xray/train/normal/IM-0257-0001.jpeg", "/chest-xray/train/normal/IM-0261-0001.jpeg", "/chest-xray/train/normal/IM-0262-0001.jpeg", "/chest-xray/train/normal/IM-0264-0001.jpeg", "/chest-xray/train/normal/IM-0265-0001.jpeg", "/chest-xray/train/normal/IM-0266-0001.jpeg", "/chest-xray/train/normal/IM-0268-0001.jpeg", "/chest-xray/train/normal/IM-0269-0001.jpeg", "/chest-xray/train/normal/IM-0270-0001.jpeg", "/chest-xray/train/normal/IM-0272-0001.jpeg", "/chest-xray/train/normal/IM-0273-0001.jpeg", "/chest-xray/train/pneumonia/", "/chest-xray/train/pneumonia/.DS_Store", "/chest-xray/train/pneumonia/person1000_bacteria_2931.jpeg", "/chest-xray/train/pneumonia/person1000_virus_1681.jpeg", "/chest-xray/train/pneumonia/person1001_bacteria_2932.jpeg", "/chest-xray/train/pneumonia/person1002_bacteria_2933.jpeg", "/chest-xray/train/pneumonia/person1003_bacteria_2934.jpeg", "/chest-xray/train/pneumonia/person1003_virus_1685.jpeg", "/chest-xray/train/pneumonia/person1004_bacteria_2935.jpeg", "/chest-xray/train/pneumonia/person1004_virus_1686.jpeg", "/chest-xray/train/pneumonia/person1005_bacteria_2936.jpeg", "/chest-xray/train/pneumonia/person1005_virus_1688.jpeg", "/chest-xray/train/pneumonia/person1006_bacteria_2937.jpeg", "/chest-xray/train/pneumonia/person1007_bacteria_2938.jpeg", "/chest-xray/train/pneumonia/person1007_virus_1690.jpeg", "/chest-xray/train/pneumonia/person1008_bacteria_2939.jpeg", "/chest-xray/train/pneumonia/person1008_virus_1691.jpeg", "/chest-xray/train/pneumonia/person1009_virus_1694.jpeg", "/chest-xray/train/pneumonia/person100_virus_184.jpeg", "/chest-xray/train/pneumonia/person1010_bacteria_2941.jpeg", "/chest-xray/train/pneumonia/person1010_virus_1695.jpeg", "/chest-xray/train/pneumonia/person1011_bacteria_2942.jpeg", "/chest-xray/train/pneumonia/person1012_bacteria_2943.jpeg", "/chest-xray/train/pneumonia/person1014_bacteria_2945.jpeg", "/chest-xray/train/pneumonia/person1015_virus_1701.jpeg", "/chest-xray/train/pneumonia/person1015_virus_1702.jpeg", "/chest-xray/train/pneumonia/person1016_bacteria_2947.jpeg", "/chest-xray/train/pneumonia/person1016_virus_1704.jpeg", "/chest-xray/train/pneumonia/person1017_bacteria_2948.jpeg", "/chest-xray/train/pneumonia/person1018_bacteria_2949.jpeg", "/chest-xray/train/pneumonia/person1018_virus_1706.jpeg", "/chest-xray/train/pneumonia/person1019_bacteria_2950.jpeg", "/chest-xray/train/pneumonia/person1019_virus_1707.jpeg", "/chest-xray/train/pneumonia/person1019_virus_1708.jpeg", "/chest-xray/train/pneumonia/person101_virus_187.jpeg", "/chest-xray/train/pneumonia/person101_virus_188.jpeg", "/chest-xray/train/pneumonia/person1020_bacteria_2951.jpeg", "/chest-xray/train/pneumonia/person1020_virus_1710.jpeg", "/chest-xray/train/pneumonia/person1021_virus_1711.jpeg", "/chest-xray/train/pneumonia/person1022_bacteria_2953.jpeg", "/chest-xray/train/pneumonia/person1022_virus_1712.jpeg", "/chest-xray/train/pneumonia/person1023_bacteria_2954.jpeg", "/chest-xray/train/pneumonia/person1023_virus_1714.jpeg", "/chest-xray/train/pneumonia/person1024_bacteria_2955.jpeg", "/chest-xray/train/pneumonia/person1024_virus_1716.jpeg", "/chest-xray/train/pneumonia/person1026_bacteria_2957.jpeg", "/chest-xray/train/pneumonia/person1026_virus_1718.jpeg", "/chest-xray/train/pneumonia/person1028_bacteria_2959.jpeg", "/chest-xray/train/pneumonia/person1028_bacteria_2960.jpeg", "/chest-xray/train/pneumonia/person1029_bacteria_2961.jpeg", "/chest-xray/train/pneumonia/person1029_virus_1721.jpeg", "/chest-xray/train/pneumonia/person102_virus_189.jpeg", "/chest-xray/train/pneumonia/person1030_virus_1722.jpeg", "/chest-xray/train/pneumonia/person1031_bacteria_2963.jpeg", "/chest-xray/train/pneumonia/person1031_bacteria_2964.jpeg", "/chest-xray/train/pneumonia/person1031_virus_1723.jpeg", "/chest-xray/train/pneumonia/person1033_bacteria_2966.jpeg", "/chest-xray/train/pneumonia/person1034_bacteria_2968.jpeg", "/chest-xray/train/pneumonia/person1034_virus_1728.jpeg", "/chest-xray/train/pneumonia/person1035_bacteria_2969.jpeg", "/chest-xray/train/pneumonia/person1035_virus_1729.jpeg", "/chest-xray/train/pneumonia/person1036_bacteria_2970.jpeg", "/chest-xray/train/pneumonia/person1036_virus_1730.jpeg", "/chest-xray/train/pneumonia/person1037_bacteria_2971.jpeg", "/chest-xray/train/pneumonia/person1038_bacteria_2972.jpeg", "/chest-xray/train/pneumonia/person1038_virus_1733.jpeg", "/chest-xray/train/pneumonia/person1039_bacteria_2973.jpeg", "/chest-xray/train/pneumonia/person103_virus_190.jpeg", "/chest-xray/train/pneumonia/person1040_bacteria_2974.jpeg", "/chest-xray/train/pneumonia/person1040_virus_1735.jpeg", "/chest-xray/train/pneumonia/person1041_bacteria_2975.jpeg", "/chest-xray/train/pneumonia/person1041_virus_1736.jpeg", "/chest-xray/train/pneumonia/person1042_virus_1737.jpeg", "/chest-xray/train/pneumonia/person1043_bacteria_2977.jpeg", "/chest-xray/train/pneumonia/person1043_virus_1738.jpeg", "/chest-xray/train/pneumonia/person1044_bacteria_2978.jpeg", "/chest-xray/train/pneumonia/person1044_virus_1740.jpeg", "/chest-xray/train/pneumonia/person1045_bacteria_2979.jpeg", "/chest-xray/train/pneumonia/person1045_virus_1741.jpeg", "/chest-xray/train/pneumonia/person1046_bacteria_2980.jpeg", "/chest-xray/train/pneumonia/person1046_virus_1742.jpeg", "/chest-xray/train/pneumonia/person1048_bacteria_2982.jpeg", "/chest-xray/train/pneumonia/person1048_virus_1744.jpeg", "/chest-xray/train/pneumonia/person1049_bacteria_2983.jpeg", "/chest-xray/train/pneumonia/person1049_virus_1746.jpeg", "/chest-xray/train/pneumonia/person104_virus_191.jpeg", "/chest-xray/train/pneumonia/person1050_bacteria_2984.jpeg", "/chest-xray/train/pneumonia/person1051_bacteria_2985.jpeg", "/chest-xray/train/pneumonia/person1051_virus_1750.jpeg", "/chest-xray/train/pneumonia/person1052_bacteria_2986.jpeg", "/chest-xray/train/pneumonia/person1052_virus_1751.jpeg", "/chest-xray/train/pneumonia/person1053_bacteria_2987.jpeg", "/chest-xray/train/pneumonia/person1054_bacteria_2988.jpeg", "/chest-xray/train/pneumonia/person1055_bacteria_2989.jpeg", "/chest-xray/train/pneumonia/person1056_bacteria_2990.jpeg", "/chest-xray/train/pneumonia/person1056_virus_1755.jpeg", "/chest-xray/train/pneumonia/person1057_bacteria_2991.jpeg", "/chest-xray/train/pneumonia/person1057_virus_1756.jpeg", "/chest-xray/train/pneumonia/person1058_bacteria_2992.jpeg", "/chest-xray/train/pneumonia/person1058_virus_1757.jpeg", "/chest-xray/train/pneumonia/person1059_bacteria_2993.jpeg", "/img/", "/img/README.md", "/img/cats/", "/img/cats/README.md", "/img/cats/cats1.jpg", "/img/cats/cats10.jpg", "/img/cats/cats11.jpg", "/img/cats/cats12.jpg", "/img/cats/cats13.jpg", "/img/cats/cats14.jpg", "/img/cats/cats15.jpg", "/img/cats/cats16.jpg", "/img/cats/cats17.jpg", "/img/cats/cats18.jpg", "/img/cats/cats19.jpg", "/img/cats/cats2.jpg", "/img/cats/cats20.jpg", "/img/cats/cats21.jpg", "/img/cats/cats22.jpg", "/img/cats/cats23.jpg", "/img/cats/cats24.jpg", "/img/cats/cats25.jpg", "/img/cats/cats26.jpg", "/img/cats/cats27.jpg", "/img/cats/cats28.jpg", "/img/cats/cats29.jpg", "/img/cats/cats3.jpg", "/img/cats/cats30.jpg", "/img/cats/cats31.jpg", "/img/cats/cats32.jpeg", "/img/cats/cats33.jpg", "/img/cats/cats34.jpg", "/img/cats/cats35.jpg", "/img/cats/cats36.jpg", "/img/cats/cats37.jpg", "/img/cats/cats38.jpg", "/img/cats/cats4.jpg", "/img/cats/cats5.jpg", "/img/cats/cats6.jpg", "/img/cats/cats7.jpg", "/img/cats/cats8.jpg", "/img/cats/cats9.jpg", "/img/dogs/", "/img/dogs/README.md", "/img/dogs/dog1.jpg", "/img/dogs/dog10.jpg", "/img/dogs/dog11.jpg", "/img/dogs/dog12.jpg", "/img/dogs/dog13.jpg", "/img/dogs/dog14.jpg", "/img/dogs/dog15.jpg", "/img/dogs/dog16.jpg", "/img/dogs/dog17.jpg", "/img/dogs/dog18.jpg", "/img/dogs/dog19.jpg", "/img/dogs/dog2.jpg", "/img/dogs/dog20.jpg", "/img/dogs/dog21.jpg", "/img/dogs/dog22.jpg", "/img/dogs/dog23.jpg", "/img/dogs/dog24.jpg", "/img/dogs/dog25.jpg", "/img/dogs/dog26.jpg", "/img/dogs/dog27.jpg", "/img/dogs/dog28.jpg", "/img/dogs/dog29.jpg", "/img/dogs/dog3.jpg", "/img/dogs/dog30.jpg", "/img/dogs/dog31.jpg", "/img/dogs/dog32.jpg", "/img/dogs/dog33.jpg", "/img/dogs/dog34.jpg", "/img/dogs/dog35.jpg", "/img/dogs/dog36.jpg", "/img/dogs/dog37.jpg", "/img/dogs/dog38.JPG", "/img/dogs/dog39.jpg", "/img/dogs/dog4.jpg", "/img/dogs/dog40.jpg", "/img/dogs/dog41.jpeg", "/img/dogs/dog42.png", "/img/dogs/dog43.png", "/img/dogs/dog5.jpg", "/img/dogs/dog6.jpg", "/img/dogs/dog7.jpg", "/img/dogs/dog8.jpg", "/img/dogs/dog9.jpg", "/img/founders/", "/img/founders/Ali-Ghodsi.jpg", "/img/founders/Reynold-Xin.jpg", "/img/founders/andy-Konwinski.jpg", "/img/founders/ionS.jpg", "/img/founders/matei.jpg", "/img/founders/patrickW.jpg", "/img/pug.jpg", "/img/rose.jpg", "/img/strawberries.jpg", "/news/", "/news/README.md", "/news/labelled_newscatcher_dataset.csv", "/reviews/", "/reviews/README.md", "/reviews/reviews_cleaned.parquet/", "/reviews/reviews_cleaned.parquet/_SUCCESS", "/reviews/reviews_cleaned.parquet/_committed_1781047980026884776", "/reviews/reviews_cleaned.parquet/_started_1781047980026884776", "/reviews/reviews_cleaned.parquet/part-00000-tid-1781047980026884776-09f36a8d-24e5-48b3-be3f-e18fe44d9e38-228-1-c000.snappy.parquet", "/reviews/reviews_cleaned.parquet/part-00001-tid-1781047980026884776-09f36a8d-24e5-48b3-be3f-e18fe44d9e38-229-1-c000.snappy.parquet", "/reviews/reviews_cleaned.parquet/part-00002-tid-1781047980026884776-09f36a8d-24e5-48b3-be3f-e18fe44d9e38-230-1-c000.snappy.parquet", "/reviews/reviews_cleaned.parquet/part-00003-tid-1781047980026884776-09f36a8d-24e5-48b3-be3f-e18fe44d9e38-231-1-c000.snappy.parquet", "/reviews/reviews_cleaned.parquet/part-00004-tid-1781047980026884776-09f36a8d-24e5-48b3-be3f-e18fe44d9e38-232-1-c000.snappy.parquet", "/reviews/reviews_cleaned.parquet/part-00005-tid-1781047980026884776-09f36a8d-24e5-48b3-be3f-e18fe44d9e38-233-1-c000.snappy.parquet", "/reviews/reviews_cleaned.parquet/part-00006-tid-1781047980026884776-09f36a8d-24e5-48b3-be3f-e18fe44d9e38-234-1-c000.snappy.parquet", "/reviews/reviews_cleaned.parquet/part-00007-tid-1781047980026884776-09f36a8d-24e5-48b3-be3f-e18fe44d9e38-235-1-c000.snappy.parquet", "/reviews/tfidf.parquet/", "/reviews/tfidf.parquet/_SUCCESS", "/reviews/tfidf.parquet/_committed_4242655036865767982", "/reviews/tfidf.parquet/_started_4242655036865767982", "/reviews/tfidf.parquet/part-00000-tid-4242655036865767982-2e9ed4a2-a403-405c-afb2-2064be60a338-705-1-c000.snappy.parquet", "/reviews/tfidf.parquet/part-00001-tid-4242655036865767982-2e9ed4a2-a403-405c-afb2-2064be60a338-698-1-c000.snappy.parquet", "/reviews/tfidf.parquet/part-00002-tid-4242655036865767982-2e9ed4a2-a403-405c-afb2-2064be60a338-702-1-c000.snappy.parquet", "/reviews/tfidf.parquet/part-00003-tid-4242655036865767982-2e9ed4a2-a403-405c-afb2-2064be60a338-700-1-c000.snappy.parquet", "/reviews/tfidf.parquet/part-00004-tid-4242655036865767982-2e9ed4a2-a403-405c-afb2-2064be60a338-703-1-c000.snappy.parquet", "/reviews/tfidf.parquet/part-00005-tid-4242655036865767982-2e9ed4a2-a403-405c-afb2-2064be60a338-699-1-c000.snappy.parquet", "/reviews/tfidf.parquet/part-00006-tid-4242655036865767982-2e9ed4a2-a403-405c-afb2-2064be60a338-701-1-c000.snappy.parquet", "/reviews/tfidf.parquet/part-00007-tid-4242655036865767982-2e9ed4a2-a403-405c-afb2-2064be60a338-704-1-c000.snappy.parquet", "/sec-fillings/", "/sec-fillings/README.md", "/sec-fillings/test-fin3.txt", "/sec-fillings/train-fin5.txt", "/wine-quality/", "/wine-quality/README.md", "/wine-quality/test/", "/wine-quality/test/_delta_log/", "/wine-quality/test/_delta_log/.s3-optimization-0", "/wine-quality/test/_delta_log/.s3-optimization-1", "/wine-quality/test/_delta_log/.s3-optimization-2", "/wine-quality/test/_delta_log/00000000000000000000.crc", "/wine-quality/test/_delta_log/00000000000000000000.json", "/wine-quality/test/part-00000-2732e96b-053b-4976-b9d0-643b9534c200-c000.snappy.parquet", "/wine-quality/test/part-00001-c4bc2dd3-2091-4adf-84a7-7d75d7033b93-c000.snappy.parquet", "/wine-quality/train/", "/wine-quality/train/_delta_log/", "/wine-quality/train/_delta_log/.s3-optimization-0", "/wine-quality/train/_delta_log/.s3-optimization-1", "/wine-quality/train/_delta_log/.s3-optimization-2", "/wine-quality/train/_delta_log/00000000000000000000.crc", "/wine-quality/train/_delta_log/00000000000000000000.json", "/wine-quality/train/part-00000-163e1699-6ec0-4e8d-9da5-f9e8bcc08b09-c000.snappy.parquet", "/wine-quality/train/part-00001-b124bcd4-f966-4b77-9998-bba681227709-c000.snappy.parquet", "/wine-quality/val/", "/wine-quality/val/_delta_log/", "/wine-quality/val/_delta_log/.s3-optimization-0", "/wine-quality/val/_delta_log/.s3-optimization-1", "/wine-quality/val/_delta_log/.s3-optimization-2", "/wine-quality/val/_delta_log/00000000000000000000.crc", "/wine-quality/val/_delta_log/00000000000000000000.json", "/wine-quality/val/part-00000-315b8ac6-511b-4c8d-a5ea-6e763dab48ea-c000.snappy.parquet", "/wine-quality/val/part-00001-eb5e9034-97a2-4828-9173-6665251f7055-c000.snappy.parquet"]

