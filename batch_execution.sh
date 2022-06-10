cd /data/jsy/code/adaptive-style-transfer/models
ls > ls.log
cd ..
for i in $( cat models/ls.log )
	do
		if [[ "$i" == "model_"* ]];then
			CUDA_VISIBLE_DEVICES=0 python main.py --model_name=$i --phase=inference --image_size=768
		fi
	done
rm -rf models/ls.log

