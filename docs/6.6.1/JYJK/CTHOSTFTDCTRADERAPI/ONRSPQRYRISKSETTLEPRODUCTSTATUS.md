<p>风险结算产品查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRISKSETTLEPRODUCTSTATUS/">ReqQryRiskSettleProductStatus</a>后，该方法被调用。</p>
<span class="anchor" id="f145e4a9-7403-4701-b7e5-88c37f895ec2"></span>
## 1.函数原型
<p>virtual void OnRspQryRiskSettleProductStatus(CThostFtdcRiskSettleProductStatusField *pRiskSettleProductStatus, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="5db68350-b185-4675-a86c-e2d85ebf359b"></span>
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
<span class="anchor" id="c192591a-0a62-4eea-a60c-e9547dca4e97"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="aabd70af-6cd7-4411-a451-c8a922c1bf53"></span>
## 4.FAQ
<p>无</p>
