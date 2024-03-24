<p>风险结算产品查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRISKSETTLEPRODUCTSTATUS/">ReqQryRiskSettleProductStatus</a>后，该方法被调用。</p>
<span class="anchor" id="17592c7e-2adb-43bd-a976-f950eab22336"></span>
## 1.函数原型
<p>virtual void OnRspQryRiskSettleProductStatus(CThostFtdcRiskSettleProductStatusField *pRiskSettleProductStatus, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="4d048c05-b2d8-48cc-9d17-030addebe2c0"></span>
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
<span class="anchor" id="cf89278c-b355-4fbb-9ae4-dd57bb909676"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="f6539523-273f-4314-9e6e-aa72b1032e47"></span>
## 4.FAQ
<p>无</p>
