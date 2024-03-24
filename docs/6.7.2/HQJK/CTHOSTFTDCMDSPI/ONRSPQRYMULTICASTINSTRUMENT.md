<p>请求查询组播合约响应</p>
<span class="anchor" id="ab87abb0-0dc8-4699-9a5f-1501720f36dc"></span>
## 1.函数原型
<p>virtual void OnRspQryMulticastInstrument(CThostFtdcMulticastInstrumentField *pMulticastInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="12221bd6-c1df-4890-9cd5-da7848491913"></span>
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
<span class="anchor" id="18edeab6-a0f9-4e1d-b33d-8da6e4aac9dd"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="03c5ebaa-a4c1-4e49-ad6e-b1d60acb7bd9"></span>
## 4.FAQ
<p>无</p>
