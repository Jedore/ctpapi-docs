<p>请求RULE品种内对锁仓折扣参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRULEINTRAPARAMETER/">ReqQryRULEIntraParameter</a>后，该方法被调用。</p>
<span class="anchor" id="ee01379c-c034-476f-a574-61ad1ab65978"></span>
## 1.函数原型
<p>virtual void OnRspQryRULEIntraParameter(CThostFtdcRULEIntraParameterField *pRULEIntraParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="e2f526e3-89af-493c-a86b-cd0398f9e68d"></span>
## 2.参数
<p>pRULEIntraParameter：RULE品种内对锁仓折扣参数</p>
<pre><code>struct CThostFtdcRULEIntraParameterField
{
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///品种代码
    TThostFtdcInstrumentIDType  ProdFamilyCode;
    ///标准合约
    TThostFtdcInstrumentIDType  StdInstrumentID;
    ///标准合约保证金
    TThostFtdcMoneyType StdInstrMargin;
    ///一般月份合约组合保证金系数
    TThostFtdcRatioType UsualIntraRate;
    ///临近交割合约组合保证金系数
    TThostFtdcRatioType DeliveryIntraRate;
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
<span class="anchor" id="e231e65b-f690-496f-800c-3843b739b159"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="1601cc32-7e28-4d0f-b28d-9943bf52e1d9"></span>
## 4.FAQ
<p>无</p>
