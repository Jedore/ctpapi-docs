<p>合约交易状态通知，主动推送。私有流回报。</p>
<p>各交易所的合约状态变化详见<a href="../../../QTYWGZ/HYZTBHSM/">合约状态变化说明</a>。</p>
<span class="anchor" id="d5329130-e789-4731-9597-e722117def1c"></span>
## 1.函数原型
<p>virtual void OnRtnInstrumentStatus(CThostFtdcInstrumentStatusField *pInstrumentStatus) {};</p>
<span class="anchor" id="e4acafc4-02ca-4129-97ea-eb5b3f7f1e28"></span>
## 2.参数
<p>pInstrumentStatus：合约状态</p>
<pre><code>struct CThostFtdcInstrumentStatusField
{
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///合约在交易所的代码
    TThostFtdcExchangeInstIDType ExchangeInstID;
    ///结算组代码
    TThostFtdcSettlementGroupIDType SettlementGroupID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///合约交易状态
    TThostFtdcInstrumentStatusType InstrumentStatus;
    ///交易阶段编号
    TThostFtdcTradingSegmentSNType TradingSegmentSN;
    ///进入本状态时间
    TThostFtdcTimeType EnterTime;
    ///进入本状态原因
    TThostFtdcInstStatusEnterReasonType EnterReason;
};
</code></pre>
<p>EnterTime：只有郑商所的时间戳是CTP的本地时间，其他交易所的是交易所时间</p>
<span class="anchor" id="c05af3b8-0f52-43f7-a5f3-d0b2beb0ba27"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="b040022a-abed-4f4c-b615-1394ebba08d8"></span>
## 4.FAQ
<p><div class="region_i" id=""><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">如何获取期权合约的状态？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>期权合约状态暂时不推送。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
