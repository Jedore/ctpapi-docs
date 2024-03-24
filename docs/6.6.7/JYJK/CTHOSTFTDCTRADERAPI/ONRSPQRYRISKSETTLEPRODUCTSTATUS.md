<p>风险结算产品查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRISKSETTLEPRODUCTSTATUS/">ReqQryRiskSettleProductStatus</a>后，该方法被调用。</p>
<span class="anchor" id="e197b565-15c7-46d6-87ca-ff11241630c3"></span>
## 1.函数原型
<p>virtual void OnRspQryRiskSettleProductStatus(CThostFtdcRiskSettleProductStatusField *pRiskSettleProductStatus, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="d24cc3d2-0975-4083-adcd-ac3ea0b46ac9"></span>
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
<span class="anchor" id="260496b2-f5fb-421e-982d-611872a022fa"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="b1ee0447-e318-4a9c-81ac-a22838e302eb"></span>
## 4.FAQ
<p>无</p>
