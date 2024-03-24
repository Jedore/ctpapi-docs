<p>请求查询组播合约响应</p>
<span class="anchor" id="cf3228e8-7043-42fa-bb76-25b199a89730"></span>
## 1.函数原型
<p>virtual void OnRspQryMulticastInstrument(CThostFtdcMulticastInstrumentField *pMulticastInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="6f0734d8-d628-461a-a7f7-66e307c756c1"></span>
## 2.参数
<p>MulticastInstrument：组播合约信息</p>
<pre><code>    struct CThostFtdcMulticastInstrumentField
    {
        ///主题号
        TThostFtdcInstallIDType TopicID;
        ///合约代码
        TThostFtdcInstrumentIDType  InstrumentID;
        ///合约编号
        TThostFtdcInstallIDType InstrumentNo;
        ///基准价
        TThostFtdcPriceType CodePrice;
        ///合约数量乘数
        TThostFtdcVolumeMultipleType    VolumeMultiple;
        ///最小变动价位
        TThostFtdcPriceType PriceTick;
    };
</code></pre>
<p>pRspInfo：错误响应</p>
<pre><code>    struct CThostFtdcRspInfoField
    {
        ///错误代码
        TThostFtdcErrorIDType ErrorID;
        ///错误信息
        TThostFtdcErrorMsgType ErrorMsg;
    };
</code></pre>
<span class="anchor" id="3571844b-0261-43f0-b504-6475818ce55c"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="28127f0e-d0a1-4bd4-b455-207ba658df8d"></span>
## 4.FAQ
<p>无</p>
