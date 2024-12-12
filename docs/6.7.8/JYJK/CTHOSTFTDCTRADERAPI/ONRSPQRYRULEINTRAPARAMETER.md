<p>请求RULE品种内对锁仓折扣参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRULEINTRAPARAMETER/">ReqQryRULEIntraParameter</a>后，该方法被调用。</p>
<span class="anchor" id="255f41c1-d55c-45f4-87f8-7996acf9230f"></span>
## 1.函数原型
<p>virtual void OnRspQryRULEIntraParameter(CThostFtdcRULEIntraParameterField *pRULEIntraParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="1ea6e3b0-8cd1-42ab-bf07-d6bde06052a9"></span>
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
<span class="anchor" id="4fe149cc-111c-48c0-8677-d99351977ce6"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="82e09faa-a07c-4513-b8b7-45b93a412283"></span>
## 4.FAQ
<p>无</p>
