<p>请求RCAMS跨品种风险折抵参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRCAMSINTERPARAMETER/">ReqQryRCAMSInterParameter</a>后，该方法被调用。</p>
<span class="anchor" id="74bc634d-817f-421f-acdc-3fbf1d387ceb"></span>
## 1.函数原型
<p>virtual void OnRspQryRCAMSInterParameter(CThostFtdcRCAMSInterParameterField *pRCAMSInterParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="fe7056e0-4b2c-466a-8e8c-84f852698fea"></span>
## 2.参数
<p>pRCAMSInterParameter：RCAMS跨品种风险折抵参数</p>
<pre><code>struct CThostFtdcRCAMSInterParameterField
{
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///商品群代码
    TThostFtdcProductIDType ProductGroupID;
    ///优先级
    TThostFtdcRCAMSPriorityType Priority;
    ///折抵率
    TThostFtdcHedgeRateType CreditRate;
    ///产品组合代码1
    TThostFtdcProductIDType CombProduct1;
    ///产品组合代码2
    TThostFtdcProductIDType CombProduct2;
};
</code></pre>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType   ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType  ErrorMsg;
};
</code></pre>
<span class="anchor" id="e102be2f-3505-4e57-a356-d7a34532c449"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="8bfc366d-fb73-4386-80fb-913c26caab73"></span>
## 4.FAQ
<p>无</p>
