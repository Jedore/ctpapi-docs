<p>风险结算产品查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRISKSETTLEPRODUCTSTATUS/">ReqQryRiskSettleProductStatus</a>后，该方法被调用。</p>
<span class="anchor" id="b24ef3ac-5d8b-4cd3-b0ce-abec44cb7b9a"></span>
## 1.函数原型
<p>virtual void OnRspQryRiskSettleProductStatus(CThostFtdcRiskSettleProductStatusField *pRiskSettleProductStatus, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="67195060-51f3-4a06-b32a-df59707a1754"></span>
## 2.参数
<p>pRiskSettleProductStatus：风险品种</p>
<pre><code>struct CThostFtdcRiskSettleProductStatusField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///产品编号
    TThostFtdcInstrumentIDType  ProductID;
    ///产品结算状态
    TThostFtdcProductStatusType ProductStatus;
};
</code></pre>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<span class="anchor" id="a0dbf146-1c9a-4adc-8f92-e0ba81b38505"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="1b0ff837-9a69-429b-b2d5-8d3f089b31ec"></span>
## 4.FAQ
<p>无</p>
