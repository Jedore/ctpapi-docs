<p>期权自对冲录入请求</p>
<p>错误响应: OnErrRtnOptionSelfCloseInsert，OnRspOptionSelfCloseInsert</p>
<p>正确响应: OnRtnOptionSelfClose</p>
<span class="anchor" id="0c3ed316-f90e-449d-8527-ed861a0c3a07"></span>
## 1.函数原型
<p>virtual int ReqOptionSelfCloseInsert(CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, int nRequestID) = 0;</p>
<span class="anchor" id="451bf0b2-d138-4c5a-8ddd-5dd543ffa553"></span>
## 2.参数
<p>pInputOptionSelfClose：输入的期权自对冲</p>
<pre><code>struct CThostFtdcInputOptionSelfCloseField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///期权自对冲引用
    TThostFtdcOrderRefType OptionSelfCloseRef;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///数量
    TThostFtdcVolumeType Volume;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///业务单元
    TThostFtdcBusinessUnitType BusinessUnit;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///期权行权的头寸是否自对冲
    TThostFtdcOptSelfCloseFlagType OptSelfCloseFlag;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
    ///资金账号
    TThostFtdcAccountIDType AccountID;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
    ///交易编码
    TThostFtdcClientIDType ClientID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="665d71ba-6749-443b-aebe-6227497dd6ba"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="f04bb484-db53-410f-94b2-2a91c8667ae7"></span>
## 4.调用示例
<pre><code>CThostFtdcInputOptionSelfCloseField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.InstrumentID, "rb1809");
strcpy_s(a.UserID, "1000001");
a.Volume = 1;
a.HedgeFlag = THOST_FTDC_HF_Speculation;
a.OptSelfCloseFlag = THOST_FTDC_OSCF_CloseSelfOptionPosition;
strcpy_s(a.ExchangeID, "SHFE");
strcpy_s(a.AccountID, "1000001");
strcpy_s(a.CurrencyID, "CNY");
m_pUserApi-&gt;ReqOptionSelfCloseInsert(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="41f6718d-4dec-4870-9969-2feec5f20582"></span>
## 5.FAQ
<p><div class="region_i" id=""><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">为什么报入的OptionSelfCloseRef和返回的值不同？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>根据交易所规则，自对冲报单由首次报入的报单属性确定，之后不论是否对该报单进行任何操作（包括撤单和重新报单），报单的OptionSelfCloseRef都不变。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
