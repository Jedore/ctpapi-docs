<p>请求RCAMS跨品种风险折抵参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRCAMSINTERPARAMETER/">ReqQryRCAMSInterParameter</a>后，该方法被调用。</p>
<span class="anchor" id="6d3250e3-23e6-4f77-80d2-65d5a235ed9c"></span>
## 1.函数原型
<p>virtual void OnRspQryRCAMSInterParameter(CThostFtdcRCAMSInterParameterField *pRCAMSInterParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="b49e95c2-adf5-4daf-a376-b3b53a10671d"></span>
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
<span class="anchor" id="939d3d6c-b6b1-4bb3-b6cb-2ec68848fa02"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="d9904ecd-a716-4a0a-a759-2802321f27e1"></span>
## 4.FAQ
<p>无</p>
