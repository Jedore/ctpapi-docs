<p>请求查询组播合约响应</p>
<span class="anchor" id="698a087a-8a18-41b8-8787-be74ec0078cb"></span>
## 1.函数原型
<p>virtual void OnRspQryMulticastInstrument(CThostFtdcMulticastInstrumentField *pMulticastInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="d93b7989-e868-4d5d-a0c3-549986878f50"></span>
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
<span class="anchor" id="d30e5d0f-7e8a-47f7-b235-7827720b364b"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="2a3ec5b1-eb9f-4969-9cdf-e406f5567d15"></span>
## 4.FAQ
<p>无</p>
