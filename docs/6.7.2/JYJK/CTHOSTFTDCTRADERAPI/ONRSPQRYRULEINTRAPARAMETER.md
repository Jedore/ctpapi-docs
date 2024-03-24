<p>请求RULE品种内对锁仓折扣参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYRULEINTRAPARAMETER/">ReqQryRULEIntraParameter</a>后，该方法被调用。</p>
<span class="anchor" id="b2f6b958-6cee-419a-aee3-99a0893007e5"></span>
## 1.函数原型
<p>virtual void OnRspQryRULEIntraParameter(CThostFtdcRULEIntraParameterField *pRULEIntraParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="62a47ee9-579d-4b0b-800b-541324592068"></span>
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
<span class="anchor" id="c807136e-f25a-4565-95d1-0d8baf01580a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="3957e251-0ebd-4584-8788-551755098a6a"></span>
## 4.FAQ
<p>无</p>
