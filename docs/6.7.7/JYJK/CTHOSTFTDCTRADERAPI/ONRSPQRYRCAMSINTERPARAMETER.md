<p>请求RCAMS跨品种风险折抵参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRCAMSINTERPARAMETER/">ReqQryRCAMSInterParameter</a>后，该方法被调用。</p>
<span class="anchor" id="4ea9e2b4-3d47-4f23-b2ba-6af7f0d41a2b"></span>
## 1.函数原型
<p>virtual void OnRspQryRCAMSInterParameter(CThostFtdcRCAMSInterParameterField *pRCAMSInterParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="99fa7255-3559-4cdc-8841-0e20e6c0b5f9"></span>
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
<span class="anchor" id="dc13ddd2-1d19-4340-b378-ef77ee8d8c30"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="fe9f9198-be3e-4d54-9770-d0a1810c0eac"></span>
## 4.FAQ
<p>无</p>
