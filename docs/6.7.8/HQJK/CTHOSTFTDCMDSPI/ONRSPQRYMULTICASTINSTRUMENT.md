<p>请求查询组播合约响应</p>
<span class="anchor" id="4898b334-9447-4a5d-820f-a1a86bc3627c"></span>
## 1.函数原型
<p>virtual void OnRspQryMulticastInstrument(CThostFtdcMulticastInstrumentField *pMulticastInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="30f2554a-cd9f-40ee-a02c-37f92d39625e"></span>
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
<span class="anchor" id="d79fa693-f9f4-43ef-be41-af042edace12"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="09e6ba5f-9524-427f-8579-7c13fed24dad"></span>
## 4.FAQ
<p>无</p>
