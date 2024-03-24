<p>报单录入请求，录入错误时对应响应OnRspOrderInsert、OnErrRtnOrderInsert，正确时对应回报OnRtnOrder、OnRtnTrade。</p>
<p>可以录入限价单、市价单、条件单等交易所支持的指令，撤单时使用ReqOrderAction。</p>
<p>不支持预埋单录入，预埋单请使用ReqParkedOrderInsert。</p>
<span class="anchor" id="749a5f08-1173-4fea-a03f-8cff4c89a8d0"></span>
## 1.函数原型
<p>virtual int ReqOrderInsert(CThostFtdcInputOrderField *pInputOrder, int nRequestID) = 0;</p>
<span class="anchor" id="8c6a9d2f-1a72-4a71-b24c-dfec2d5fb674"></span>
## 2.参数
<p>pInputOrder：输入报单</p>
<pre><code>struct CThostFtdcInputOrderField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///报单引用
    TThostFtdcOrderRefType OrderRef;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///报单价格条件
    TThostFtdcOrderPriceTypeType OrderPriceType;
    ///买卖方向
    TThostFtdcDirectionType Direction;
    ///组合开平标志
    TThostFtdcCombOffsetFlagType CombOffsetFlag;
    ///组合投机套保标志
    TThostFtdcCombHedgeFlagType CombHedgeFlag;
    ///价格
    TThostFtdcPriceType LimitPrice;
    ///数量
    TThostFtdcVolumeType VolumeTotalOriginal;
    ///有效期类型
    TThostFtdcTimeConditionType TimeCondition;
    ///GTD日期
    TThostFtdcDateType GTDDate;
    ///成交量类型
    TThostFtdcVolumeConditionType VolumeCondition;
    ///最小成交量
    TThostFtdcVolumeType MinVolume;
    ///触发条件
    TThostFtdcContingentConditionType ContingentCondition;
    ///止损价
    TThostFtdcPriceType StopPrice;
    ///强平原因
    TThostFtdcForceCloseReasonType ForceCloseReason;
    ///自动挂起标志
    TThostFtdcBoolType IsAutoSuspend;
    ///业务单元
    TThostFtdcBusinessUnitType BusinessUnit;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///用户强评标志
    TThostFtdcBoolType UserForceClose;
    ///互换单标志
    TThostFtdcBoolType IsSwapOrder;
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
<p>OrderPriceType：确定输入的报单类型，比如限价单则填写<code>THOST_FTDC_OPT_LimitPrice</code>、市价单则填写<code>THOST_FTDC_OPT_AnyPrice</code>。</p>
<p>Direction：确定买卖方向</p>
<p>CombOffsetFlag：确定开平标志。注:上期所、能源交易所有平今指令，下平仓指令和平昨指令相同</p>
<p>CombHedgeFlag：确定投机套保标志 例:投机 <code>THOST_FTDC_BHF_Speculation</code></p>
<p>TimeCondition：确定报单有效期类型 例:立即完成，否则撤销 <code>THOST_FTDC_TC_IOC</code></p>
<p>VolumeCondition：确定成交量类型</p>
<p>ContingentCondition：确定触发条件</p>
<p>StopPrice：止损价，用于条件单的触发价格</p>
<p>ForceCloseReason：普通用户下单填写<code>THOST_FTDC_FCC_NotForceClose</code> 非强平</p>
<p>IsSwapOrder：互换单填1</p>
<p>CurrencyID：不填写默认为CNY</p>
<p>OrderRef：OrderRef是本地会话全局唯一编号，必须保持递增；可由用户维护，也可由系统自动填写。一定为数字。</p>
<p>IPAddress：手工填写本机IP地址，不自动获取。</p>
<p>MacAddress：手工填写本机Mac地址，不自动获取。</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="e248bbc2-a592-4fcf-858e-41194502a0fc"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="fa86c6e3-6618-4c8e-8ebd-793fcc3db567"></span>
## 4.调用示例
<pre><code>//限价单:
CThostFtdcInputOrderField ord = { 0 };
strcpy_s(ord.BrokerID, “0000”);
strcpy_s(ord.InvestorID, “00001”); 
strcpy_s(ord.ExchangeID, “SHFE”);
strcpy_s(ord.InstrumentID, “ag1801”);
strcpy_s(ord.UserID, “00001”);
ord.OrderPriceType = THOST_FTDC_OPT_LimitPrice;//限价
ord.Direction = THOST_FTDC_D_Buy;//买
ord.CombOffsetFlag[0] = THOST_FTDC_OF_Open;//开
ord.CombHedgeFlag[0] = THOST_FTDC_HF_Speculation;//投机
ord.LimitPrice = 100;
ord.VolumeTotalOriginal = 1;
ord.TimeCondition = THOST_FTDC_TC_GFD;///当日有效
ord.VolumeCondition = THOST_FTDC_VC_AV;///任意数量
ord.MinVolume = 1;
ord.ContingentCondition = THOST_FTDC_CC_Immediately;
ord.StopPrice = 0;
ord.ForceCloseReason = THOST_FTDC_FCC_NotForceClose;
ord.IsAutoSuspend = 0;
m_pUserApi-&gt;ReqOrderInsert(&amp;ord, nRequestID++);
</code></pre>
<span class="anchor" id="889903de-954b-457d-a339-cd9b347984a8"></span>
## 5.FAQ
<p><div class="region_i" id=""><p class="region_header" id="region_header_1" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">郑商所白糖期权的跨式和宽跨式套利指令，在ctp里如何实现？</p><div class="region_panel" id="region_panel_1" style="display:block;"><table><tr><td>
<p>和普通的限价单类似，不同的地方是在填写InstrumentID的时候</p>
<p>郑商所跨式组合（STD）: STD SR703C5300&amp;SR703P5300</p>
<p>郑商所宽跨式组合（STG): STG SR703C5300&amp;SR703P5200</p>
<p>支持FAK和FOK</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_1" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i" id=""><p class="region_header" id="region_header_2" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">“已撤单报单被拒绝CZCE:出错:不支持无限制期权组合订单”是什么原因？</p><div class="region_panel" id="region_panel_2" style="display:block;"><table><tr><td>
<p>郑商所的组合合约下单，TimeCondition应该用<code>THOST_FTDC_TC_IOC</code>（1）。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_2" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i" id=""><p class="region_header" id="region_header_3" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">如果下单后遇到报错“ctp：每秒报单数超过许可数”，是什么原因？</p><div class="region_panel" id="region_panel_3" style="display:block;"><table><tr><td>
<p>这是由于报单频率太快被前置流控所致。投资者可询问期货公司具体的流控设置；期货公司可以自行查看FLEX"程序化交易频繁报撤单管理"中的设置，以及Front的流控配置。注意：Front的流控会放到下一秒，不会报错；FLEX"程序化交易频繁报撤单管理"中的流控会报错。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_3" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i" id=""><p class="region_header" id="region_header_4" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">“CTP:报单错误：不允许重复报单”，是什么原因？</p><div class="region_panel" id="region_panel_4" style="display:block;"><table><tr><td>
<p>这是表示OrderRef没有递增。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_4" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i" id=""><p class="region_header" id="region_header_5" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">“CTP:无此权限”，是什么原因？</p><div class="region_panel" id="region_panel_5" style="display:block;"><table><tr><td>
<p>这可能InvestorID填写错误，或者该InvestorID不属于UserID的组织架构下。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_5" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i" id=""><p class="region_header" id="region_header_6" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">“CTP:交易所未处理请求超过许可数”，是什么原因？</p><div class="region_panel" id="region_panel_6" style="display:block;"><table><tr><td>
<p>表示报单频率过快，超过了交易所的流控。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_6" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
<p><div class="region_i" id=""><p class="region_header" id="region_header_7" style="padding-left: 1em;font-weight : bold;text-indent: 0px;text-align: left;">“CTP:交易所每秒发送请求数超过许可数”，是什么原因？</p><div class="region_panel" id="region_panel_7" style="display:block;"><table><tr><td>
<p>表示报单频率过快，超过了交易所的流控。</p>
</td></tr></table>
</div><p class="region_tail" id="region_tail_7" style="border-top-color:transparent;border-bottom-width:0;"></p></div></p>
