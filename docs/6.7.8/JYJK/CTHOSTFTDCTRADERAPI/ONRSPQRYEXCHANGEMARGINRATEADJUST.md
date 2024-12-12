<p>请求查询交易所调整保证金率响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYEXCHANGEMARGINRATEADJUST/">ReqQryExchangeMarginRateAdjust</a>后，该方法被调用。</p>
<span class="anchor" id="211ae9f8-28cf-4ecd-ae20-f6709d231e60"></span>
## 1.函数原型
<p>virtual void OnRspQryExchangeMarginRateAdjust(CThostFtdcExchangeMarginRateAdjustField *pExchangeMarginRateAdjust, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="32bac282-546e-4af9-a94d-541a0ec5f125"></span>
## 2.参数
<p>pExchangeMarginRateAdjust：交易所保证金率调整</p>
<pre><code>struct CThostFtdcExchangeMarginRateAdjustField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///跟随交易所投资者多头保证金率
    TThostFtdcRatioType LongMarginRatioByMoney;
    ///跟随交易所投资者多头保证金费
    TThostFtdcMoneyType LongMarginRatioByVolume;
    ///跟随交易所投资者空头保证金率
    TThostFtdcRatioType ShortMarginRatioByMoney;
    ///跟随交易所投资者空头保证金费
    TThostFtdcMoneyType ShortMarginRatioByVolume;
    ///交易所多头保证金率
    TThostFtdcRatioType ExchLongMarginRatioByMoney;
    ///交易所多头保证金费
    TThostFtdcMoneyType ExchLongMarginRatioByVolume;
    ///交易所空头保证金率
    TThostFtdcRatioType ExchShortMarginRatioByMoney;
    ///交易所空头保证金费
    TThostFtdcMoneyType ExchShortMarginRatioByVolume;
    ///不跟随交易所投资者多头保证金率
    TThostFtdcRatioType NoLongMarginRatioByMoney;
    ///不跟随交易所投资者多头保证金费
    TThostFtdcMoneyType NoLongMarginRatioByVolume;
    ///不跟随交易所投资者空头保证金率
    TThostFtdcRatioType NoShortMarginRatioByMoney;
    ///不跟随交易所投资者空头保证金费
    TThostFtdcMoneyType NoShortMarginRatioByVolume;
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
<span class="anchor" id="59be7ae5-db0c-47fd-800f-643979e97054"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="26c6e372-326b-4960-a76c-860cfe9bd29c"></span>
## 4.FAQ
<p><span alt="" id="anchor-id-01"></span> </p>
<p><div class="region_i"><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">跟随交易所多头保证金率，交易所多头保证金率，不跟随交易所多头保证金率，这三个有什么区别？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>投资者交易所保证金率分两种属性（跟随交易所，不跟随交易所）</p>
<p>跟随交易所：投资者交易所保证金率=max(期货公司交易所保证金率，跟随交易所投资者多头保证金率+交易所多头保证金率)</p>
<p>不跟随交易所：投资者交易所保证金率=不跟随交易所投资者多头保证金率</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
