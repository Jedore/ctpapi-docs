<p>请求查询合约手续费率响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINSTRUMENTCOMMISSIONRATE/">ReqQryInstrumentCommissionRate</a>后，该方法被调用。</p>
<span class="anchor" id="50a87d0f-2349-47ec-9695-9d73adfdff98"></span>
## 1.函数原型
<p>virtual void OnRspQryInstrumentCommissionRate(CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="c4c70478-02fc-4bb5-a215-5bc96b55e390"></span>
## 2.参数
<p>pInstrumentCommissionRate：合约手续费率</p>
<pre><code>struct CThostFtdcInstrumentCommissionRateField
{
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///投资者范围
    TThostFtdcInvestorRangeType InvestorRange;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///开仓手续费率
    TThostFtdcRatioType OpenRatioByMoney;
    ///开仓手续费
    TThostFtdcRatioType OpenRatioByVolume;
    ///平仓手续费率
    TThostFtdcRatioType CloseRatioByMoney;
    ///平仓手续费
    TThostFtdcRatioType CloseRatioByVolume;
    ///平今手续费率
    TThostFtdcRatioType CloseTodayRatioByMoney;
    ///平今手续费
    TThostFtdcRatioType CloseTodayRatioByVolume;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///业务类型
    TThostFtdcBizTypeType   BizType;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
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
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="e6af00a3-7517-489f-8c2f-b794338bdb7e"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="1ffa4f4b-97d4-49f6-a4fd-11464d1ddc91"></span>
## 4.FAQ
<p>无</p>
