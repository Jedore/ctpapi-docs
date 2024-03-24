<p>风险结算产品查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRISKSETTLEPRODUCTSTATUS/">ReqQryRiskSettleProductStatus</a>后，该方法被调用。</p>
<span class="anchor" id="3f488cf3-f703-4d56-a729-20158557bdf6"></span>
## 1.函数原型
<p>virtual void OnRspQryRiskSettleProductStatus(CThostFtdcRiskSettleProductStatusField *pRiskSettleProductStatus, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="6eec27db-c863-440d-9ca6-6b62445498c7"></span>
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
<span class="anchor" id="5e0bebcc-d862-45e3-b885-2021477a9492"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="d1e0b2bf-6b9d-48a0-a925-49f425d366bc"></span>
## 4.FAQ
<p>无</p>
